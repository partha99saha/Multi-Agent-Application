from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(question: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=[{"role": "user", "content": question}]
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error occurred: {e}")
        return "I could not find that information."
