import { useState } from "react";
import {
    FaPaperPlane,
    FaStop,
} from "react-icons/fa";

function ChatInput({
    onSend,
    loading,
    onCancel,
}) {
    const [input, setInput] =
        useState("");

    const send = () => {
        if (!input.trim()) return;

        onSend(input);
        setInput("");
    };

    const handleKeyDown = (
        e
    ) => {
        if (e.key === "Enter") {
            send();
        }
    };

    return (
        <div className="chat-input">
            <input
                value={input}
                placeholder="Ask CortexAI..."
                onChange={(e) =>
                    setInput(
                        e.target.value
                    )
                }
                onKeyDown={
                    handleKeyDown
                }
            />

            {loading ? (
                <button
                    className="cancel-btn"
                    onClick={onCancel}
                >
                    <FaStop />
                </button>
            ) : (
                <button
                    className="send-btn"
                    onClick={send}
                >
                    <FaPaperPlane />
                </button>
            )}
        </div>
    );
}

export default ChatInput;