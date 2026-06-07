import { useEffect, useState } from "react";

export default function Sidebar() {

    const [sessions, setSessions] = useState([]);

    useEffect(() => {

        const history =
            JSON.parse(
                localStorage.getItem("session_history")
            ) || [];

        setSessions(history);

    }, []);

    return (
        <div className="sidebar">

            <h2>CortexAI</h2>

            <button>
                New Chat
            </button>

            <div className="sessions">

                {sessions.map((s, idx) => (
                    <div key={idx}>
                        {s}
                    </div>
                ))}

            </div>

        </div>
    );
}