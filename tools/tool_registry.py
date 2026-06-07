# tools/tool_registry.py

TOOLS = {}


def register_tool(name):
    def wrapper(func):
        TOOLS[name] = func
        return func

    return wrapper


def get_tool(name):
    if name not in TOOLS:
        raise Exception(f"Tool not found: {name}")
    return TOOLS[name]


def list_tools():
    return list(TOOLS.keys())
