from tools.tool_registry import get_tool
from backend.planner import create_plan
from backend.token_optimizer import optimize_context
from backend.safety import safety_check


def execute(question: str):

    plan = create_plan(question)

    context = None
    answer = None

    for step in plan:

        # STEP 1: retrieve context
        if step == "retrieve_context":
            tool = get_tool("rag")
            context = tool(question)

        # STEP 2: analyze (LLM refinement step)
        elif step == "analyze_context":
            tool = get_tool("llm")
            answer = tool(str(context))

        # STEP 3: generate final answer
        elif step == "generate_answer":
            tool = get_tool("llm")

            optimized_input = optimize_context(question, context)
            answer = tool(optimized_input)

        # STEP 4: direct answer fallback
        elif step == "direct_answer":
            tool = get_tool("llm")
            answer = tool(question)

    # SAFETY CHECK
    final = safety_check(answer)

    return {"plan": plan, "answer": final}
