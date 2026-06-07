import Loader from "./Loader";

export default function ChatWindow({
    messages,
    loading,
}) {

    return (
        <div className="chat-window">

            {messages.map((msg, idx) => (

                <div
                    key={idx}
                    className={`message ${msg.role}`}
                >
                    {msg.content}
                </div>

            ))}

            {loading && <Loader />}

        </div>
    );
}