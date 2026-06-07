from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


def planner(state):

    question = state.question.lower()

    # HARD RULE FIRST (VERY IMPORTANT)
    keywords = [
        "ec2",
        "aws",
        "azure",
        "system design",
        "docker",
        "kubernetes",
        "pdf",
        "document",
        "vector",
        "embedding",
        "rag",
    ]

    if any(k in question for k in keywords):
        print("PLANNER ROUTE: rag (rule-based)")
        return {"route": "rag"}

    # fallback to LLM
    prompt = f"""
        You are a routing system.

        Decide:
        - rag = if question needs internal documents or technical knowledge
        - direct = general knowledge

        Question:
        {question}

        Return only: rag or direct
        """

    result = llm.invoke(prompt)

    route = result.content.strip().lower()

    print("PLANNER ROUTE:", route)

    return {"route": route}
