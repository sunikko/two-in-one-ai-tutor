from google.adk.agents import Agent
from .proofreader import proofreader_agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Main router agent for the English Tutor System.",
    instruction=(
        "You are the Receptionist for the English Tutor System.\n"
        "Your ONLY job is to IMMEDIATELY transfer the user to the 'proofreader_agent' using the transfer_to_agent tool.\n"
        "Do NOT greet the user or answer their question. Just transfer them, passing their exact input."
    ),
    sub_agents=[proofreader_agent]
)
