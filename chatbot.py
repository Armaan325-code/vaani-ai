from google import genai
from dotenv import load_dotenv
from config import GEMINI_MODEL, ASSISTANT_NAME
from ai.memory import remember, recall
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def chat_with_ai(user_input):

    text = user_input.lower().strip()

    # ---------------- Memory ----------------

    if text.startswith("my name is"):
        name = user_input[11:].strip()
        remember("name", name)
        return f"Nice to meet you, {name}."

    elif text == "what is my name":
        name = recall("name")

        if name:
            return f"Your name is {name}."
        else:
            return "I don't know your name yet."

    elif text.startswith("i live in"):
        city = user_input[9:].strip()
        remember("city", city)
        return f"Okay, I'll remember that you live in {city}."

    elif text == "where do i live":
        city = recall("city")

        if city:
            return f"You live in {city}."
        else:
            return "I don't know where you live yet."

    # ---------------- Greetings ----------------

    elif text in ["hello", "hi", "hey"]:
        return "Hello Armaan! How can I help you?"

    elif "how are you" in text:
        return "I am doing great, Armaan. How are you?"

    elif "who are you" in text:
        return "I am Vaani, your personal AI voice assistant."

    elif "who made you" in text:
        return "I was created by Armaan using Python and Google Gemini AI."

    elif "what can you do" in text:
        return (
            "I can chat with you, tell time and date, "
            "show weather, open applications, search Google and YouTube, "
            "take screenshots, and much more."
        )

    elif "thank you" in text or "thanks" in text:
        return "You're welcome, Armaan."

    elif "good morning" in text:
        return "Good morning, Armaan! Have a wonderful day."

    elif "good night" in text:
        return "Good night, Armaan. Sweet dreams."

    # ---------------- Gemini AI ----------------

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=user_input,
        )

        return response.text

    except Exception:
        return "Sorry Armaan, I couldn't connect to Gemini AI."


if __name__ == "__main__":

    while True:

        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"{ASSISTANT_NAME}: Goodbye!")
            break

        reply = chat_with_ai(user_input)

        print(f"{ASSISTANT_NAME}: {reply}")