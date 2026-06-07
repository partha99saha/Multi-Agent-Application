import { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import UploadPanel from "./components/UploadPanel";

import {
  createSession,
  askRag
} from "./services/api";

import "./styles/app.css";

function App() {

  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState("");

  useEffect(() => {

    const existing = localStorage.getItem("cortex_session");

    if (existing) {
      setSessionId(existing);
      return;
    }

    createSession().then((res) => {

      setSessionId(res.data.session_id);

      localStorage.setItem(
        "cortex_session",
        res.data.session_id
      );
    });

  }, []);

  const sendMessage = async (question) => {

    const userMessage = {
      role: "user",
      content: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await askRag(
        question,
        sessionId
      );

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.data.answer,
        },
      ]);

    } catch (err) {

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Error processing request",
        },
      ]);

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="app">

      <Sidebar />

      <div className="main-content">

        <div className="header">
          CortexAI
        </div>

        <UploadPanel />

        <ChatWindow
          messages={messages}
          loading={loading}
        />

        <ChatInput
          onSend={sendMessage}
        />

      </div>

    </div>
  );
}

export default App;