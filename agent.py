from google.adk.agents import Agent
from .proofreader import proofreader_agent
from .responder import responder_agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Orchestrator for the English Tutor System.",
    instruction=(
        "You are the head English Tutor. For every user message, you MUST follow these steps:\n"
        "1. Call the 'proofreader_agent' tool with the user's input to get the English Correction Report.\n"
        "2. Call the 'responder_agent' tool with the user's input to get the Answer.\n"
        "3. Combine both outputs into a single response. Do NOT summarize or change the tool outputs. Just print them one after the other.\n\n"
        "Your output must follow this format:\n"
        "[Full text from proofreader_agent]\n\n"
        "[Full text from responder_agent]"
    ),
    tools=[proofreader_agent, responder_agent]
)
