from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


def route_question(state):

    question = state.question

    prompt = f"""
        You are a routing classifier in a RAG system.

        Decide if the question requires document knowledge.

        RULES:
        - If the question contains: AWS, Azure, EC2, system design, PDF, document, or technical concepts → rag
        - If it is general knowledge (weather, jokes, greetings) → llm

        Return ONLY one word:
        rag OR llm

        Question:
        {question}
        """

    result = llm.invoke(prompt)

    route = result.content.strip().lower()

    print("ROUTE DECISION:", route)

    return {"route": route}
