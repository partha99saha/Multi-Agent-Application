import { useEffect, useState } from "react";
import axios from "axios";

import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import TopBar from "./components/TopBar";

import "./styles/app.css";

function App() {
  const [sessions, setSessions] = useState([]);
  const [currentSession, setCurrentSession] = useState(null);

  const [messages, setMessages] = useState([]);

  const [mode, setMode] = useState("rag");

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem("cortex_sessions");

    if (saved) {
      const parsed = JSON.parse(saved);

      setSessions(parsed);

      if (parsed.length > 0) {
        setCurrentSession(parsed[0].id);
        setMessages(parsed[0].messages || []);
      }
    }
  }, []);

  const createNewSession = () => {

    if (sessions.length >= 2) {
      alert("Maximum 2 sessions allowed");
      return;
    }

    const now = new Date();

    const title =
      now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      });

    const newSession = {
      id: Date.now(),
      title,
      messages: [],
    };

    const updated = [newSession, ...sessions];

    setSessions(updated);
    setCurrentSession(newSession.id);
    setMessages([]);

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify(updated)
    );
  };

  const updateSessionMessages = (
    sessionId,
    newMessages
  ) => {
    const updated = sessions.map((s) =>
      s.id === sessionId
        ? {
          ...s,
          messages: newMessages,
        }
        : s
    );

    setSessions(updated);

    localStorage.setItem(
      "cortex_sessions",
      JSON.stringify(updated)
    );
  };

  const sendMessage = async (question) => {
    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      content: question,
    };

    const newMessages = [
      ...messages,
      userMessage,
    ];

    setMessages(newMessages);

    setLoading(true);

    try {
      let response;

      if (mode === "rag") {
        response = await axios.get(
          "http://localhost:8000/rag",
          {
            params: {
              question,
              session_id: "ui-session",
            },
          }
        );
      } else if (mode === "llm") {
        response = await axios.get(
          "http://localhost:8000/ask",
          {
            params: { question },
          }
        );
      } else if (mode === "image") {
        response = await axios.get(
          "http://localhost:8000/image",
          {
            params: { prompt: question },
          }
        );
      } else {
        response = await axios.get(
          "http://localhost:8000/audio",
          {
            params: { text: question },
          }
        );
      }

      const aiMessage = {
        role: "assistant",
        content:
          response.data.answer ||
          JSON.stringify(response.data),
      };

      const updatedMessages = [
        ...newMessages,
        aiMessage,
      ];

      setMessages(updatedMessages);

      updateSessionMessages(
        currentSession,
        updatedMessages
      );
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  const uploadFile = async (file) => {
    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {
      await axios.post(
        "http://localhost:8000/upload",
        formData
      );

      alert("Upload successful");
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  };

  return (
    <div className="app">
      <Sidebar
        sessions={sessions}
        currentSession={currentSession}
        setCurrentSession={(id) => {
          setCurrentSession(id);
          const session =
            sessions.find(
              (s) => s.id === id
            );
          if (session) {
            setMessages(
              session.messages || []
            );
          }
        }}
        createNewSession={createNewSession}
        uploadFile={uploadFile}
      />

      <div className="main-content">
        <TopBar
          mode={mode}
          setMode={setMode}
        />

        <ChatWindow
          messages={messages}
        />

        <ChatInput
          onSend={sendMessage}
          loading={loading}
        />
      </div>
    </div>
  );
}

export default App;