import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOGETHER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.together.xyz/v1"
)

def chat_with_bot():
    print("🤖 AI Chatbot (type 'exit' to quit)\n")

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",  
            messages=messages,
            temperature=0.7
        )

        bot_reply = response.choices[0].message.content
        print(f"Bot: {bot_reply}")

        messages.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    chat_with_bot()
