# 🇬🇧 English Tutor Multi-Agent System

This repository contains an AI-powered "2-in-1" English Tutor built using the **Google Agentic Development Kit (ADK)** and the Gemini API.

## 🌟 Overview
Unlike a standard chatbot, this system uses a **Multi-Agent Architecture** to perform two distinct tasks simultaneously when you ask a question in English:
1. **Grammar Correction**: It catches broken English, awkward phrasing, and grammatical errors, providing a detailed correction report.
2. **Helpful Response**: It understands the underlying intent of your question and provides a natural, deep answer.

By separating these tasks into specialized agents, you get both English tutoring and an actual helpful answer in a single combined output!

## 🏗️ Architecture

The system consists of three agents working together:

- **Root Agent (Orchestrator)** (`agent.py`): The main router. It receives the user's input and strictly forces both sub-agents to run. It then beautifully combines their outputs into a final response.
- **Proofreader Agent** (`proofreader.py`): Powered by `gemini-2.5-flash`. Its sole purpose is to analyze the English input, correct it, and explain *why* it was corrected, without answering the actual question.
- **Responder Agent** (`responder.py`): Powered by `gemini-2.5-flash`. Its sole purpose is to deeply answer the actual question being asked, ignoring grammatical errors to focus entirely on context and intent.

*(Note: Both sub-agents use `gemini-2.5-flash` to ensure lightning-fast execution times and avoid Free Tier quota limitations.)*

## 🚀 Getting Started

### Prerequisites
- Python Environment with Google ADK installed.
- A valid Google Gemini API Key.

### Installation & Setup

1. **Clone the repository** (if applicable).
2. **Set up your environment variables**:
   Create a `.env` file in the root of `english_tutor_agent` and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
3. **Run the Agent**:
   Navigate to the **parent directory** of `english_tutor_agent` (e.g., your workspace root) and run the ADK web server:
   ```bash
   cd ..
   adk web
   ```
4. **Test it out!**:
   Open the provided local URL (usually `http://127.0.0.1:8000`), select `english_tutor_agent`, and ask a question with intentional bad grammar (e.g., *"What is you favorite foods?"*).

## 🛠️ Tech Stack
- **Framework**: Google ADK (Agentic Development Kit)
- **Model**: Gemini 2.5 Flash
- **Language**: Python 3
