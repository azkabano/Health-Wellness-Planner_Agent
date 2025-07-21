from agent import health_planner_agent 
from context import UserSessionContext
from agents import Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
from dotenv import load_dotenv
from agents.run import RunConfig
import asyncio, os
from utils.streaming import stream_response

load_dotenv()
set_tracing_disabled(disabled=True)
API_KEY = os.getenv("GEMINI_API_KEY")


external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client
)


print("*" * 5 ,"Health and Wellness AI Agent", "*" * 5,"\n")
print("Type 'exit' or 'quit' to Finish.\n")

History_save = []

async def main():
    user_context = UserSessionContext(name="khaid", uid=1001)
    while True:
        prompt = input("🧑 You :")
        if prompt.lower() in ['exit',"quit"]:
            print("👋 Goodbye!")
            break

        # save user prompt
        user_context.messages.append({"role": "user", "content": prompt})

        result = Runner.run_streamed(
            health_planner_agent,
            prompt,
            context=user_context,
            run_config=config)
        
        # Use the streaming handler
        await stream_response(result, user_context)

        #  Save assistant reply
        user_context.messages.append({"role": "assistant", "content": result.final_output})


if __name__ == "__main__":
      asyncio.run(main())