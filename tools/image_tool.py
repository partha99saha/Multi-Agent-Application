from tools.tool_registry import register_tool
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@register_tool("image")
def generate_image(prompt: str):

    response = client.images.generate(model="dall-e-3", prompt=prompt, size="1024x1024")

    return {"image_url": response.data[0].url}
