import "./../styles/sidebar.css";

export default function Sidebar({
    sessions,
    currentSession,
    setCurrentSession,
    createNewSession,
    uploadFile,
}) {
    return (
        <aside className="sidebar">
            <div className="sidebar-top">
                <h1 className="logo">CortexAI</h1>

                <button
                    className="new-chat-btn"
                    onClick={createNewSession}
                >
                    + New Chat
                </button>

                <div className="sessions-container">
                    <h3>Sessions</h3>

                    <div className="sessions-list">
                        {sessions.map((session) => (
                            <div
                                key={session.id}
                                className={`session-item ${currentSession === session.id ? "active" : ""
                                    }`}
                                onClick={() =>
                                    setCurrentSession(session.id)
                                }
                            >
                                {session.title}
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            <div className="sidebar-bottom">
                <div className="upload-card">
                    <h4>Upload Knowledge</h4>

                    <input
                        id="fileUpload"
                        type="file"
                        hidden
                        onChange={(e) =>
                            uploadFile(e.target.files[0])
                        }
                    />

                    <button
                        className="upload-btn"
                        onClick={() =>
                            document
                                .getElementById("fileUpload")
                                .click()
                        }
                    >
                        Upload Files
                    </button>
                </div>

                <div className="health-card">
                    <h4>System Health</h4>

                    <div className="health-item">
                        <span className="green-dot"></span>
                        Backend API
                    </div>

                    <div className="health-item">
                        <span className="green-dot"></span>
                        Vector DB
                    </div>

                    <div className="health-item">
                        <span className="green-dot"></span>
                        LLM Service
                    </div>
                </div>
            </div>
        </aside>
    );
}