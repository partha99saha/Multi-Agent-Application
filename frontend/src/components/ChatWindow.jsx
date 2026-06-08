function ChatWindow({
    messages,
}) {

    return (
        <div className="chat-window">

            {messages.length === 0 ? (

                <div className="welcome">

                    <h1>CortexAI</h1>

                    <p>
                        Enterprise Knowledge &
                        Agent Platform
                    </p>

                </div>

            ) : (

                messages.map((msg, index) => (

                    <div
                        key={index}
                        className={
                            msg.role === "user"
                                ? "user-message"
                                : "ai-message"
                        }
                    >
                        {msg.content}
                    </div>

                ))

            )}

        </div>
    );
}

export default ChatWindow;