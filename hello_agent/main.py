import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


# Gemini as LLM Provider
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Model Configuration
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# RunConfig
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
# Main Agent Logic
async def main():
    agent = Agent(
        name= "Assistant",
        instructions="You only respond in haikus",
        model = model
    )
    
    #  Running the Agent
    user_question = input("\nEnter your Prompt/Question: ")
    
    print("=" * 60)
    print("\n🤖 HELLO AGENT - DEMO CONVERSATION\n")
    print("=" * 60)
    print(f"👤 User:\n{user_question}\n")
    
    result = await Runner.run(agent, user_question, run_config=config)
    
    print("🧠 Assistant (in haiku):")
    print("-" * 60)
    print(result.final_output)
    print("=" * 60)
    
if __name__ == "__main__":
    asyncio.run(main())