from openai import OpenAI
from dotenv import load_dotenv
import os

from utils.timer import timeit
from utils.prompt_cache import get_cached_response, set_cached_response
from backend.session_manager import is_cancelled

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@timeit("llm_call")
def ask_llm(question, session_id=None, task_id=None):

    # ---------------------------
    # CANCEL CHECK (EARLY EXIT)
    # ---------------------------
    if session_id and task_id and is_cancelled(session_id, task_id):
        return "Cancelled"

    # ---------------------------
    # CACHE CHECK
    # ---------------------------
    cached = get_cached_response(question)
    if cached:
        print("[CACHE HIT]")
        return cached

    # ---------------------------
    # FINAL CANCEL CHECK BEFORE CALL
    # ---------------------------
    if session_id and task_id and is_cancelled(session_id, task_id):
        return "Cancelled"

    # ---------------------------
    # OPENAI CALL
    # ---------------------------
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": question}]
    )

    answer = response.choices[0].message.content

    # ---------------------------
    # STORE CACHE
    # ---------------------------
    set_cached_response(question, answer)

    return answer


# ---------------------------
# LOCAL TEST
# ---------------------------
if __name__ == "__main__":
    q = input("Question: ")
    print(ask_llm(q))
