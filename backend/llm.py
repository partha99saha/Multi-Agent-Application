from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
from utils.prompt_cache import get_cached_response, set_cached_response
from utils.timer import timeit

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@timeit("llm_call")
def ask_llm(question: str):

    # 1. check cache first
    cached = get_cached_response(question)
    if cached:
        print("[CACHE HIT]")
        return cached

    # 2. call OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": question}]
    )

    # return response.choices[0].message.content
    answer = response.choices[0].message.content

    # 3. store in cache
    set_cached_response(question, answer)

    return answer
