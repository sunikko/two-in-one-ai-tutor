# V1: The "Fake Orchestrator" Architecture (For Practice Reference)

This document serves as a historical record of the initial V1 architecture that was committed for practice purposes.

## The Problem
Initially, the Multi-Agent System was designed with a central `root_agent` that was supposed to:
1. Pass the user's input to `proofreader_agent`.
2. Pass the user's input to `responder_agent`.
3. Combine both outputs into a single message.

However, Google ADK's `sub_agents` feature fundamentally uses a **Handoff (Transfer)** mechanism (`transfer_to_agent`). 
It does NOT execute sub-agents as subroutines returning strings to the caller.

## The "Scam" (Why it seemed to work initially)
The first few times this system was run, it appeared to work perfectly. Why?
Because the `root_agent` (using `gemini-2.5-flash`) ignored its instruction to call the tools, and instead **hallucinated** both the grammar correction and the answer by itself. It acted as a Single Agent pretending to be a Multi-Agent system.

Once we explicitly forced the `root_agent` to use the tools (by forbidding it from generating the answer itself), it correctly called `transfer_to_agent("proofreader_agent")`.
But because `transfer_to_agent` is a handoff, the `root_agent` "hung up the phone" and disappeared. The `proofreader_agent` gave its answer, but the `responder_agent` was never called, and the outputs were never combined.

## The Solution
To build a TRUE multi-agent system within ADK's handoff constraints, the architecture must be refactored into a **Daisy Chain (Relay) Pattern**, which is documented in `v2_relay_architecture.md`.
