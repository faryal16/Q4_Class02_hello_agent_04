# 🤖 Hello Agent – OpenAI Agents SDK Demo

This project demonstrates how to use the **OpenAI Agents SDK** with **Google Gemini** as a custom LLM provider inside a `uv`-managed Python environment.

## 📁 Project Structure: `hello_agent/`

```text
hello_agent/
├── main.py           # Main Python script running the agent
├── .env              # Contains your GEMINI_API_KEY
├── README.md         # Project documentation
└── uv virtual env    # Created by uv init
```

## ⚙️ Setup Instructions

1. **Clone or navigate to the project folder:**

   ```bash
   cd hello_agent
   ```
2. **Install dependencies using uv:**

```bash
uv add openai-agents python-dotenv
```
3. **Create a .env file with your Gemini key:**

```env
GEMINI_API_KEY=your_google_gemini_key
```

## 🚀 Run the Agent
```bash

uv run main.py
```

## ✅ Sample Output
```text
============================================================
🤖 HELLO AGENT - DEMO CONVERSATION
============================================================
👤 User:
What is the meaning of true friendship?

🧠 Assistant (in haiku):
------------------------------------------------------------
Hearts speak without words,  
Storms may come, yet roots hold firm,  
Time tests, love endures.
============================================================
```
## 🧠 Agent Behavior
This agent is configured with:

- Model: gemini-2.0-flash

- Instructions: "You only respond in haikus"

## 📚 References

- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Google Gemini OpenAI-Compatible API](https://ai.google.dev/gemini-api/docs/openai)



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

