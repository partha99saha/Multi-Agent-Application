from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


def critic_node(state):

    answer = state.draft_answer
    context = state.context

    prompt = f"""
    You are a critic agent.

    Check if the answer is grounded in the context.

    If correct → return SAME answer
    If wrong → fix it using context

    Context:
    {context}

    Answer:
    {answer}
    """

    result = llm.invoke(prompt)

    return {"final_answer": result.content}
