
# 📁 Project Overview
This project demonstrates the use of the OpenAI Agents SDK with a custom LLM provider (Google Gemini) and is divided into two parts:

## 📂 1. hello_agent/
This folder contains a working example of an agent built using the OpenAI Agents SDK with a virtual environment managed by uv. It includes:
- ✅ A virtual environment using uv
- ✅ main.py code that:
    - Loads a Gemini API key from .env
    - Initializes a Gemini client
    - Creates an Agent with haiku-style instructions
    - Sends a user question and prints the assistant's haiku response

## Run Instructions:
```bash
cd hello_agent
uv run main.py
```

Make sure .env file contains:
```ini
GEMINI_API_KEY=your_api_key_here
```

## 📂 2. openai_agent_sdk/
This folder includes a single file:
- 📄 README.md (this file)
It explains the inner working of the OpenAI Agents SDK, focusing on:
- Agent creation
- Custom LLM provider configuration
- RunConfig setup
- Execution using Runner.run()
No code is needed here — just conceptual understanding.

### ✅ Summary
| Folder             | Purpose                         |
|--------------------|----------------------------------|
| `hello_agent`      | Practical demo with code         |
| `openai_agent_sdk` | Documentation of internal logic  |