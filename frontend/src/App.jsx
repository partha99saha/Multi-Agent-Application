import { useEffect, useState } from "react";
import axios from "axios";
import Sidebar from "./components/Sidebar";
import TopBar from "./components/TopBar";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import "./styles/app.css";

function App() {
  const [sessions, setSessions] = useState([]);
  const [currentSession, setCurrentSession] = useState(null);

  const [messages, setMessages] = useState([]);

  const [mode, setMode] = useState("rag");

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem(
      "cortex_sessions"
    );

    if (saved) {
      const parsed = JSON.parse(saved);

      setSessions(parsed);

      if (parsed.length > 0) {
        setCurrentSession(parsed[0].id);
        setMessages(
          parsed[0].messages || []
        );
      }
    }
  }, []);

  const createNewSession = () => {
    if (sessions.length >= 2) {
      alert(
        "Maximum 2 sessions allowed"
      );
      return;
    }

    const now = new Date();

    const title = `chat-${new Date()
      .toISOString()
      .slice(11, 19)
      .replaceAll(":", "-")}`;

    const newSession = {
      id: Date.now(),
      title,
      messages: [],
    };

    const updated = [
      newSession,
      ...sessions,
    ];

    setSessions(updated);
    setCurrentSession(newSession.id);
    setMessages([]);

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify(updated)
    );
  };

  const deleteSession = (id) => {
    const updated =
      sessions.filter(
        (s) => s.id !== id
      );

    setSessions(updated);

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify(updated)
    );

    if (updated.length > 0) {
      setCurrentSession(
        updated[0].id
      );

      setMessages(
        updated[0].messages || []
      );
    } else {
      setCurrentSession(null);
      setMessages([]);
    }
  };

  const saveMessagesToSession = (
    sessionId,
    msgs
  ) => {
    const updated = sessions.map(
      (s) =>
        s.id === sessionId
          ? {
            ...s,
            messages: msgs,
          }
          : s
    );

    setSessions(updated);

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify(updated)
    );
  };

  const sendMessage = async (
    question
  ) => {
    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      content: question,
    };

    const tempMessages = [
      ...messages,
      userMessage,
    ];

    setMessages(tempMessages);

    setLoading(true);

    try {
      let response;

      if (mode === "rag") {
        response = await axios.get(
          "http://localhost:8000/rag",
          {
            params: {
              question,
              session_id:
                "frontend-session",
            },
          }
        );
      } else if (
        mode === "llm"
      ) {
        response = await axios.get(
          "http://localhost:8000/ask",
          {
            params: { question },
          }
        );
      } else if (
        mode === "image"
      ) {
        response = await axios.get(
          "http://localhost:8000/image",
          {
            params: {
              prompt: question,
            },
          }
        );
      } else {
        response = await axios.get(
          "http://localhost:8000/audio",
          {
            params: {
              text: question,
            },
          }
        );
      }

      const aiMessage = {
        role: "assistant",
        content:
          response.data.answer ||
          JSON.stringify(
            response.data
          ),
      };

      const updatedMessages = [
        ...tempMessages,
        aiMessage,
      ];

      setMessages(updatedMessages);

      saveMessagesToSession(
        currentSession,
        updatedMessages
      );

      await new Promise(
        (resolve) =>
          setTimeout(resolve, 300)
      );
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  const uploadFile = async (
    file
  ) => {
    if (!file) return;

    const formData =
      new FormData();

    formData.append(
      "file",
      file
    );

    try {
      await axios.post(
        "http://localhost:8000/upload",
        formData
      );

      alert(
        "File uploaded successfully"
      );
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="app">
      <Sidebar
        sessions={sessions}
        currentSession={
          currentSession
        }
        setCurrentSession={(
          id
        ) => {
          setCurrentSession(id);

          const session =
            sessions.find(
              (s) =>
                s.id === id
            );

          if (session) {
            setMessages(
              session.messages ||
              []
            );
          }
        }}
        createNewSession={
          createNewSession
        }
        deleteSession={
          deleteSession
        }
        uploadFile={
          uploadFile
        }
      />

      <div className="main-content">
        <TopBar
          mode={mode}
          setMode={setMode}
        />

        <ChatWindow
          messages={messages}
          loading={loading}
        />

        <ChatInput
          onSend={sendMessage}
          loading={loading}
          onCancel={() => {
            setLoading(false);
          }}
        />
      </div>
    </div>
  );
}

export default App;