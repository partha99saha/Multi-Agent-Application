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
            {messages.length === 0 && !loading && (
                <div className="welcome">
                    <h1 className="welcome-title">
                        CortexAI
                    </h1>
                    <p className="welcome-subtitle">
                        Enterprise Knowledge & Agent Platform
                    </p>
                    <p className="welcome-desc">
                        Multi-Agent AI • Hybrid RAG • Multimodal Tools • LangGraph Orchestration
                    </p>
                </div>
            )}

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
                            {/* {msg.content} */}
                            <>
                                {msg.type === "image" ? (
                                    <img
                                        src={`http://localhost:8000/${msg.content}`}
                                        className="chat-image"
                                        alt="generated"
                                    />
                                ) : msg.type === "audio" ? (
                                    <audio controls className="chat-audio">
                                        <source
                                            src={`http://localhost:8000/${msg.content}`}
                                            type="audio/mpeg"
                                        />
                                    </audio>
                                ) : (
                                    <div>{msg.content}</div>
                                )}

                                <div className="message-footer">
                                    {msg.time && (
                                        <span>
                                            {msg.time}
                                        </span>
                                    )}
                                    {msg.duration && (
                                        <span>
                                            • {msg.duration}s
                                        </span>
                                    )}
                                </div>
                            </>
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