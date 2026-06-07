from tools.tool_registry import get_tool
from backend.planner import create_plan
from backend.token_optimizer import optimize_context
from backend.safety import safety_check
from backend.model_selector import select_model
from backend.mcp import build_mcp


def execute(question: str):

    plan = create_plan(question)

    context = None
    answer = None

    try:

        for step in plan:

            if step == "retrieve_context":
                tool = get_tool("rag")
                context = tool(question)

            elif step == "generate_answer":
                tool = get_tool("llm")

                optimized = optimize_context(question, context)

                model = select_model(question, context)

                mcp_payload = build_mcp(question, context, plan, model)

                answer = tool(optimized)

        final = safety_check(answer)

        return {"plan": plan, "model_used": model, "answer": final, "mcp": mcp_payload}

    except Exception as e:

        return {"error": str(e), "fallback": "System failed safely"}
