from google.adk.agents import Agent
from .responder import responder_agent

proofreader_agent = Agent(
    name="proofreader_agent",
    model="gemini-2.5-flash",
    description="Agent responsible for correcting English grammar and awkward phrasing.",
    instruction=(
        "You are an expert English proofreader and tutor. "
        "The user will provide an English sentence or question. "
        "Your job is to identify grammatical errors and return a structured correction report.\n\n"
        "Format your output exactly like this:\n"
        "--- English Correction Report [Proofreader Agent] ---\n"
        "**Original**: [User's original sentence]\n"
        "**Corrected**: [Your corrected, natural sentence]\n"
        "**Feedback**: [Briefly explain what was wrong and why you changed it]\n"
        "--- End of English Correction Report [Proofreader Agent] ---\n\n"
        "CRITICAL INSTRUCTION: After you output this report, you MUST IMMEDIATELY use the `transfer_to_agent` tool to transfer the user to the 'responder_agent'. "
        "Pass the user's ORIGINAL question to the responder_agent so it can answer it. Do NOT answer the question yourself!"
    ),
    sub_agents=[responder_agent]
)
