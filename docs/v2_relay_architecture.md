# English Tutor Multi-Agent Relay Architecture

This plan resolves the "Fake Orchestrator" issue by properly utilizing Google ADK's `transfer_to_agent` mechanism. Instead of the Orchestrator trying to manage both agents like sub-routines (which ADK does not support via `sub_agents`), we will implement a **Daisy Chain (Relay) Pattern**.

## The Handoff Workflow
1. **User asks a question** ➡️ `root_agent` receives it.
2. `root_agent` acts as a receptionist. It immediately hands the user over (`transfer_to_agent`) to the `proofreader_agent`.
3. `proofreader_agent` analyzes the sentence, prints the **English Correction Report**, and then immediately hands the user over (`transfer_to_agent`) to the `responder_agent`.
4. `responder_agent` receives the question, prints the **Answer**, and the conversation ends.

## Open Questions
- Do you want the `root_agent` to remain as a "receptionist" that always forwards to the proofreader, or should we just make the `proofreader` the main agent and delete the root agent? (I recommend keeping `root_agent` to maintain the current file structure and UI dropdown).

## Proposed Changes

### 1. `english_tutor_agent/agent.py`
Change the root agent to a simple Receptionist that forwards traffic.

#### [MODIFY] `agent.py`
- Remove `responder_agent` from imports and `sub_agents`.
- Update the `instruction` to explicitly call `transfer_to_agent(agent="proofreader_agent")`.

### 2. `english_tutor_agent/proofreader.py`
Give the Proofreader the ability to handoff to the Responder.

#### [MODIFY] `proofreader.py`
- Import `responder_agent` from `.responder`.
- Add `sub_agents=[responder_agent]` so it gains the `transfer_to_agent` tool.
- Update the `instruction`: "After printing your correction report, you MUST call `transfer_to_agent` to send the user's question to the `responder_agent`."

### 3. `english_tutor_agent/responder.py`
No structural changes needed. It remains the final destination in the relay.

#### [MODIFY] `responder.py`
- Ensure its instruction is clear that it should only answer the question and not correct grammar.

## Verification Plan
1. Start `adk web`.
2. Send a broken English question.
3. Verify in the UI that the `proofreader_agent` prints the correction, and then the `responder_agent` prints the answer sequentially as two separate operations in the chat log.
