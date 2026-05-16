# V3: The "Pro" Orchestrator Architecture (AgentTool Pattern)

This document explains the final and most robust version of the English Tutor
Multi-Agent System, built using Google ADK's `AgentTool`.

---

## The Full Evolution: Why We Arrived Here

### V1 — Fake Orchestrator (Single Agent Hallucination)
The very first version used a single `root_agent` with `sub_agents=[proofreader, responder]`.
- **What we expected**: The root agent would call both sub-agents and combine their output.
- **What actually happened**: ADK's `sub_agents` only provides a `transfer_to_agent` handoff tool.
  The root agent simply *pretended* to run the sub-agents and generated the output itself.
- **Verdict**: ❌ Not a real multi-agent system. Just a single agent with a fake costume.

---

### V2 — Relay/Daisy-Chain (Handoff Pattern)
We refactored so that `root_agent` → `proofreader_agent` → `responder_agent` using `transfer_to_agent`.
- **What worked**: Each agent genuinely ran independently. True multi-agent behavior.
- **What failed**: Once control was transferred to `responder_agent`, it became the active
  agent for the entire session. The second question bypassed the proofreader entirely.
- **Root cause**: `sub_agents` = "department transfer". The session stays with the last agent.
- **Verdict**: ✅ Real multi-agent, but ❌ single-turn pipeline only. Breaks on the 2nd message.

---

### V3 — Orchestrator with AgentTool (Final Solution) ✅
We used ADK's official `AgentTool` class to wrap sub-agents as callable tools.

```python
from google.adk.tools.agent_tool import AgentTool

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    tools=[
        AgentTool(agent=proofreader_agent),
        AgentTool(agent=responder_agent),
    ]
)
```

- **What works**: The `root_agent` retains full control of the session at all times.
  It calls `proofreader_agent` and `responder_agent` as sub-routines (tools), waits for
  their responses, and combines the result.
- **Multi-turn**: Because `root_agent` never transfers its session, every new message
  starts a fresh orchestration cycle through both tools automatically.
- **Verdict**: ✅ True multi-agent. ✅ Persistent multi-turn conversation.

---

## Key Concept: `sub_agents` vs `tools=[AgentTool(...)]`

| Feature               | `sub_agents=[agent]`                   | `tools=[AgentTool(agent)]`             |
|-----------------------|----------------------------------------|----------------------------------------|
| Who controls session? | Transferred to sub-agent               | Always the root agent                  |
| Pattern name          | Handoff / Relay                        | Orchestrator / Subroutine              |
| Multi-turn support    | ❌ Requires session reset              | ✅ Works seamlessly                    |
| Output control        | Sub-agent responds directly to user    | Root agent combines & formats output   |
| Use case              | Simple pipeline, one-shot delegation   | Complex orchestration, continuous chat |

---

## Final Architecture

```
User Input
    │
    ▼
root_agent (Orchestrator — always in control)
    ├── calls AgentTool(proofreader_agent) ──► Returns: Grammar Correction Report
    └── calls AgentTool(responder_agent)   ──► Returns: Helpful Answer
    │
    ▼
Combined output displayed to the user
```
