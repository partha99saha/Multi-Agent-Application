import { useState } from "react";

function ChatInput({
    onSend,
    loading,
}) {

    const [input, setInput] =
        useState("");

    const handleSend = () => {

        if (!input.trim()) return;

        onSend(input);

        setInput("");
    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter") {
            handleSend();
        }
    };

    return (
        <div className="chat-input">

            <input
                value={input}
                placeholder="Ask CortexAI..."
                onChange={(e) =>
                    setInput(e.target.value)
                }
                onKeyDown={handleKeyDown}
            />

            <button
                onClick={handleSend}
                disabled={loading}
            >
                {loading ? "..." : "Send"}
            </button>

        </div>
    );
}

export default ChatInput;