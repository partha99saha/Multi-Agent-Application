class MCPMessage:
    def __init__(self, tool, input, context=None):
        self.tool = tool
        self.input = input
        self.context = context
