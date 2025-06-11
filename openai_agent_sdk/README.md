 
# 🤖 OpenAI Agents SDK – Inner Working Overview

This document explains the **inner working** of the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), using **Google Gemini** as the LLM provider.

---

## ✅ What is the Agents SDK?

OpenAI's Agents SDK simplifies building AI assistants (agents) that can:
- Understand instructions
- Use tools
- Manage context
- Call LLMs (OpenAI or others like Gemini)

---

## 🧩 Key Components in the SDK

### 1. `AsyncOpenAI` – Custom LLM Provider

Used to connect to **non-OpenAI LLMs**, like Gemini, using the OpenAI-compatible API structure.

```python
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```

### 2. OpenAIChatCompletionsModel – Model Adapter
Wraps the Gemini model into a format the SDK understands.

```python
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
```

### 3. RunConfig – Execution Settings
Provides configuration to the agent runner, such as model and client.

```python
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
```

### 4. Agent – The Assistant
Defines the assistant’s personality, style, and behavior.

```python
agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=model
)
```

### 5. Runner – Executes the Agent
Used to pass the user’s prompt and get a response.

```python

result = await Runner.run(agent, "What is true friendship?", run_config=config)
print(result.final_output)
```

## 🧠 Flow Summary
``` pgsql
.env file → Load API key
      ↓
AsyncOpenAI → Gemini client
      ↓
OpenAIChatCompletionsModel → model wrapper
      ↓
Agent + Runner → run the assistant with user input
```

## 📝 Example Prompt and Output
User Input

- "What is true friendship?"

Agent Output (Haiku)

```pgsql
Hearts that walk as one,  
Lifting each other through storms—  
Roots deeper than time.
```

## 📂 Folder Content
```sql
openagent-sdk/
└── README.md   # ← This file (inner working explanation only)
```

## ✅ Purpose
This folder demonstrates the internal structure and logic of the OpenAI Agents SDK using a custom Gemini-based model. It's not a code folder, but a concept explanation repo.
