import { useEffect, useRef } from "react";

function ChatWindow({
    messages,
    loading,
}) {
    const bottomRef = useRef(null);
    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });

    }, [messages, loading]);

    return (
        <div className="chat-window">

            {messages.map(
                (msg, index) => (
                    <div
                        key={index}
                        className={`message-row ${msg.role === "user"
                            ? "user-row"
                            : "assistant-row"
                            }`}
                    >
                        <div
                            className={`message-bubble ${msg.role === "user"
                                ? "user-bubble"
                                : "assistant-bubble"
                                }`}
                        >
                            {msg.content}
                        </div>
                    </div>
                )
            )}

            {loading && (
                <div className="assistant-row">
                    <div className="thinking">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            )}
            <div ref={bottomRef} />
        </div>
    );
}

export default ChatWindow;