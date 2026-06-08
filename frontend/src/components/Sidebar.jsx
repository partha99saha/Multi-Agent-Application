import "../styles/sidebar.css";
import {
    FaTrash,
} from "react-icons/fa";

function Sidebar({
    sessions,
    currentSession,
    setCurrentSession,
    createNewSession,
    deleteSession,
    uploadFile,
}) {
    return (
        <aside className="sidebar">
            <div>
                <h1 className="logo">
                    CortexAI
                </h1>

                <button
                    className="new-chat-btn"
                    onClick={
                        createNewSession
                    }
                >
                    + New Chat
                </button>

                <h3>Sessions</h3>

                <div className="sessions-list">
                    {sessions.map(
                        (session) => (
                            <div
                                key={session.id}
                                className={`session-item ${currentSession ===
                                    session.id
                                    ? "active"
                                    : ""
                                    }`}
                                onClick={() =>
                                    setCurrentSession(
                                        session.id
                                    )
                                }
                            >
                                <span>
                                    {
                                        session.title
                                    }
                                </span>

                                <button
                                    className="delete-btn"
                                    onClick={(e) => {
                                        e.stopPropagation();

                                        deleteSession(
                                            session.id
                                        );
                                    }}
                                >
                                    <FaTrash />
                                </button>
                            </div>
                        )
                    )}
                </div>
            </div>

            <div>
                <div className="upload-card">
                    <h4>
                        Upload
                        Knowledge
                    </h4>

                    <input
                        hidden
                        id="uploadInput"
                        type="file"
                        onChange={(e) =>
                            uploadFile(
                                e.target
                                    .files[0]
                            )
                        }
                    />

                    <button
                        onClick={() =>
                            document
                                .getElementById(
                                    "uploadInput"
                                )
                                .click()
                        }
                    >
                        Upload Files
                    </button>
                </div>

            </div>
        </aside>
    );
}

export default Sidebar;