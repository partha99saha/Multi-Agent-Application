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
  const [uploadMessage,
    setUploadMessage] =
    useState("");

  useEffect(() => {
    const saved = localStorage.getItem(
      "cortex_sessions"
    );

    if (saved) {
      const parsed = JSON.parse(saved);
      if (parsed.length > 0) {
        setSessions(parsed);
        setCurrentSession(
          parsed[0].id
        );
        setMessages(
          parsed[0].messages || []
        );
        return;
      }
    }

    const defaultSession = {
      id: Date.now(),
      title: `chat-${new Date()
        .toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        })}`,
      messages: [],
    };

    setSessions([defaultSession]);

    setCurrentSession(
      defaultSession.id
    );

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify([
        defaultSession,
      ])
    );

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

  const switchSession = (
    sessionId
  ) => {

    const session =
      sessions.find(
        (s) =>
          s.id === sessionId
      );

    if (!session) return;

    setCurrentSession(
      sessionId
    );

    setMessages(
      session.messages || []
    );
  };

  const deleteSession = (id) => {
    const updated =
      sessions.filter(
        (s) => s.id !== id
      );

    if (updated.length === 0) {

      const defaultSession = {
        id: Date.now(),
        title: `chat-${new Date()
          .toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })}`,
        messages: [],
      };

      setSessions([
        defaultSession,
      ]);

      setCurrentSession(
        defaultSession.id
      );

      setMessages([]);

      localStorage.setItem(
        "cortex_sessions",
        JSON.stringify([
          defaultSession,
        ])
      );

      return;
    }

    setSessions(updated);

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify(updated)
    );

    setCurrentSession(
      updated[0].id
    );

    setMessages(
      updated[0].messages || []
    );
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

      setUploadMessage(
        "✅ Knowledge Base Updated"
      );
    } catch (err) {
      console.error(err);
    }
  };


  return (
    <div className="app">
      <Sidebar
        sessions={sessions}
        uploadMessage={uploadMessage}
        switchSession={switchSession}
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