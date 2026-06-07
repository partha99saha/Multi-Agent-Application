import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

export const createSession = () =>
    api.post("/session/create");

export const askQuestion = (question) =>
    api.get("/ask", {
        params: { question },
    });

export const askRag = (question, sessionId) =>
    api.get("/rag", {
        params: {
            question,
            session_id: sessionId,
        },
    });

export const uploadFile = (file) => {
    const formData = new FormData();

    formData.append("file", file);

    return api.post("/upload", formData);
};

export default api;