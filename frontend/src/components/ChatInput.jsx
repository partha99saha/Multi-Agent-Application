import { useState } from "react";

export default function ChatInput({
    onSend,
}) {

    const [text, setText] = useState("");

    const submit = () => {

        if (!text.trim()) return;

        onSend(text);

        setText("");

    };

    return (
        <div className="chat-input">

            <input
                value={text}
                onChange={(e) =>
                    setText(e.target.value)
                }
                placeholder="Ask CortexAI..."
            />

            <button onClick={submit}>
                Send
            </button>

        </div>
    );
}