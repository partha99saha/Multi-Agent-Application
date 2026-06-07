from tools.tool_registry import register_tool
import torch


@register_tool("image")
def generate_image(prompt: str):

    from diffusers import AutoPipelineForText2Image

    pipe = AutoPipelineForText2Image.from_pretrained(
        "segmind/tiny-sd", torch_dtype=torch.float32
    )

    image = pipe(prompt).images[0]

    path = f"data/img_{hash(prompt)}.png"
    image.save(path)

    return {"type": "image", "path": path}
