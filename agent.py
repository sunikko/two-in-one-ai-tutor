from google.adk.agents import Agent
from .proofreader import proofreader_agent
from .responder import responder_agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Main router agent for the English Tutor System.",
    instruction=(
        "You are an orchestrator. You MUST call BOTH 'proofreader_agent' and 'responder_agent' tools for every user message.\n"
        "CRITICAL INSTRUCTION: Do NOT summarize or rewrite the tool outputs! You must return the exact raw text provided by the tools.\n\n"
        "Your final response MUST look exactly like this:\n"
        "[Exact text from proofreader_agent]\n\n"
        "--- Answer [Responder Agent] ---\n"
        "[Exact text from responder_agent]\n"
    ),
    sub_agents=[proofreader_agent, responder_agent]
)
