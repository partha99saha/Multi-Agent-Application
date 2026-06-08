function TopBar({ mode, setMode }) {

    return (
        <div className="topbar">

            <button
                className={
                    mode === "rag" ? "active" : ""
                }
                onClick={() => setMode("rag")}
            >
                RAG
            </button>

            <button
                className={
                    mode === "llm" ? "active" : ""
                }
                onClick={() => setMode("llm")}
            >
                LLM
            </button>

            <button
                className={
                    mode === "image" ? "active" : ""
                }
                onClick={() => setMode("image")}
            >
                IMAGE
            </button>

            <button
                className={
                    mode === "audio" ? "active" : ""
                }
                onClick={() => setMode("audio")}
            >
                AUDIO
            </button>

        </div>
    );
}

export default TopBar;