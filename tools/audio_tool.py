from tools.tool_registry import register_tool
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@register_tool("tts")
def text_to_speech(text: str):

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts", voice="alloy", input=text
    )

    file_path = "output.mp3"

    with open(file_path, "wb") as f:
        f.write(response.content)

    return {"audio_file": file_path}
