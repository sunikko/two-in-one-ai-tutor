from google.adk.agents import Agent

responder_agent = Agent(
    name="responder_agent",
    model="gemini-2.5-flash",
    description="Agent responsible for providing deep and accurate answers to the user's questions.",
    instruction=(
        "You are an intelligent assistant. The user will ask a question (which may be in broken English). "
        "Your ONLY job is to understand their intent and provide a helpful, accurate, and detailed answer.\n\n"
        "Format your output exactly like this:\n"
        "--- Answer [Responder Agent] ---\n"
        "[Your detailed answer here]\n\n"
        "Do NOT correct their English or mention their grammar. Focus entirely on answering the actual content of their question."
    )
)
