# 🇬🇧 English Tutor Multi-Agent System

This repository contains an AI-powered "2-in-1" English Tutor built using the **Google Agentic Development Kit (ADK)** and the Gemini API.

## 🌟 Overview
Unlike a standard chatbot, this system uses a **Multi-Agent Architecture** to perform two distinct tasks for every question you ask in English:
1. **Grammar Correction**: It catches broken English, awkward phrasing, and grammatical errors, providing a detailed correction report.
2. **Helpful Response**: It understands the underlying intent of your question and provides a natural, deep answer.

By separating these tasks into specialized agents, you get both English tutoring and an actual helpful answer in a single combined output — in every message, continuously.

---

## 🏗️ Architecture

The system consists of three agents working together using the **`AgentTool` Orchestrator Pattern**:

- **Root Agent (Orchestrator)** (`agent.py`): The brain of the system. It retains full session control and calls the other two agents as tools via `AgentTool`, then combines their outputs into one response.
- **Proofreader Agent** (`proofreader.py`): Powered by `gemini-2.5-flash`. Its sole purpose is to analyze the English input, correct it, and explain *why* it was corrected — without answering the actual question.
- **Responder Agent** (`responder.py`): Powered by `gemini-2.5-flash`. Its sole purpose is to deeply answer the actual question, ignoring grammatical errors to focus entirely on context and intent.

```
User Input
    │
    ▼
root_agent (Orchestrator — always in control)
    ├── AgentTool(proofreader_agent) ──► Returns: Grammar Correction Report
    └── AgentTool(responder_agent)   ──► Returns: Helpful Answer
    │
    ▼
Combined output displayed to the user
```

---

## 📖 Architectural Evolution

This project went through three distinct versions before arriving at the final design. Each version exposed a deeper understanding of how Google ADK actually works.

### V1 — Fake Orchestrator ❌
Used `sub_agents=[proofreader, responder]` on the root agent.
- **What we expected**: Root agent calls both sub-agents and combines output.
- **What actually happened**: ADK's `sub_agents` only provides a `transfer_to_agent` handoff tool. The root agent simply *pretended* to run them and generated output by itself.
- **Verdict**: Not a real multi-agent system.

### V2 — Relay / Daisy-Chain ⚠️
Refactored so that `root_agent` → `proofreader_agent` → `responder_agent` using `transfer_to_agent`.
- **What worked**: Each agent genuinely ran independently. True multi-agent behavior.
- **What failed**: Once control transferred to `responder_agent`, it became the active agent for the rest of the session. The second question bypassed the proofreader entirely.
- **Root cause**: `sub_agents` = "department transfer". The session stays with the last agent.
- **Verdict**: Real multi-agent, but single-turn pipeline only. Breaks on the 2nd message.

### V3 — `AgentTool` Orchestrator ✅ (Final)
Used ADK's official `AgentTool` to wrap sub-agents as callable tools for the orchestrator.
- **What works**: The `root_agent` retains full session control. It calls both agents as sub-routines, waits for their responses, and combines the result.
- **Multi-turn**: Because `root_agent` never transfers its session, every new message triggers both tools automatically.
- **Verdict**: True multi-agent. Persistent multi-turn conversation.

### Key Difference: `sub_agents` vs `AgentTool`

| Feature               | `sub_agents=[agent]`              | `tools=[AgentTool(agent)]`         |
|-----------------------|-----------------------------------|------------------------------------|
| Session control       | Transferred to sub-agent          | Always the root agent              |
| Pattern name          | Handoff / Relay                   | Orchestrator / Subroutine          |
| Multi-turn support    | ❌ Requires session reset         | ✅ Works seamlessly                |
| Output control        | Sub-agent responds directly       | Root agent combines & formats      |
| Use case              | Simple pipeline, one-shot         | Complex orchestration, continuous  |

---

## 🛠️ Tech Stack
- **Framework**: Google ADK (Agentic Development Kit)
- **Model**: Gemini 2.5 Flash
- **Language**: Python 3
