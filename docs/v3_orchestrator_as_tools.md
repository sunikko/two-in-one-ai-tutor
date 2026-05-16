# V3: The "Pro" Orchestrator Architecture (Agents as Tools)

This is the final, most advanced version of the English Tutor Multi-Agent System.

## The Evolution
1. **V1 (Fake Orchestrator)**: Single agent hallucinating results. Broken when tool-calling was forced.
2. **V2 (Relay/Handoff)**: agents transferred control (`transfer_to_agent`). Correct but limited to single-turn pipelines (requires session reset for new questions).
3. **V3 (Agents as Tools)**: The `root_agent` uses sub-agents as **Subroutines (Tools)**. This is the gold standard for complex agentic systems.

## Why this is better
- **Continuous Conversation**: The `root_agent` remains the active agent throughout the entire session. You can ask 100 questions in one chat window, and it will call the tools every time.
- **True Orchestration**: The `root_agent` actually waits for the sub-agents to finish their "job" and then combines their reports into a single, beautifully formatted response.
- **Robustness**: No circular imports, no session reset issues, and perfect control over the final UI output.

## How it works
- `agent.py` uses `tools=[proofreader_agent, responder_agent]`.
- When the user asks a question, `root_agent` calls both tools, gets the raw text back, and prints it.
- Because it's a tool call, not a handoff, the session context stays with the orchestrator.
