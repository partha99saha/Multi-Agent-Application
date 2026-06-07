from tools.tool_registry import register_tool
import pyttsx3

engine = pyttsx3.init()


@register_tool("tts")
def text_to_speech(text: str):

    path = f"data/audio_{hash(text)}.mp3"

    engine.save_to_file(text, path)
    engine.runAndWait()

    return {"type": "audio", "path": path}
