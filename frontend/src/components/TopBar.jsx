function TopBar({ mode, setMode }) {

    return (
        <div className="topbar">
            <span className="topbar-title">AI Playground </span> 
            <button
                className={
                    mode === "rag"
                        ? "topbar-btn active"
                        : "topbar-btn"
                }
                onClick={() => setMode("rag")}
            >
                RAG
            </button>

            <button
                className={
                    mode === "llm"
                        ? "topbar-btn active"
                        : "topbar-btn"
                }
                onClick={() => setMode("llm")}
            >
                LLM
            </button>

            {/* <button
                className={
                    mode === "image"
                        ? "topbar-btn active"
                        : "topbar-btn"
                }
                onClick={() => setMode("image")}
            >
                IMAGE
            </button>

            <button
                className={
                    mode === "audio"
                        ? "topbar-btn active"
                        : "topbar-btn"
                }
                onClick={() => setMode("audio")}
            >
                AUDIO
            </button> */}

        </div>
    );
}

export default TopBar;