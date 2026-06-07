# tools/tool_registry.py

TOOLS = {}


def register_tool(name: str):
    def decorator(func):
        TOOLS[name] = func
        return func

    return decorator


def get_tool(name: str):
    return TOOLS.get(name)


def list_tools():
    return list(TOOLS.keys())
