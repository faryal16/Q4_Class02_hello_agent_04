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


