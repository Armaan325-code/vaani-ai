from google import genai
from dotenv import load_dotenv
from config import GEMINI_MODEL, ASSISTANT_NAME
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def chat_with_ai(user_input):
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=user_input,
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"{ASSISTANT_NAME}: Goodbye!")
            break

        reply = chat_with_ai(user_input)
        print(f"{ASSISTANT_NAME}:", reply)