import asyncio

from chatbot import chat_with_ai
from speaker import speak
from config import ASSISTANT_NAME

from commands.features import get_time, get_date
from commands.battery_commands import get_battery
from commands.screenshot_commands import take_screenshot
from commands.weather_commands import get_weather
from commands.help_commands import get_help

from commands.system_commands import (
    open_notepad,
    open_calculator,
    open_paint,
    open_cmd,
    open_explorer,
    open_downloads
)

from commands.web_commands import (
    open_google,
    open_youtube,
    open_github,
    open_gmail,
    search_google,
    search_youtube
)


def main():

    print(f"{ASSISTANT_NAME} Started!")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            reply = "Goodbye!"
            print(f"{ASSISTANT_NAME}: {reply}")
            asyncio.run(speak(reply))
            break

        # Time

        elif user_input == "time":
            reply = get_time()

        # Date

        elif user_input == "date":
            reply = get_date()

        elif user_input=="help":
            reply = get_help()   

        # Weather

        elif user_input == "weather":
            reply = get_weather()

        elif user_input.startswith("weather in"):
            city = user_input.replace("weather in", "").strip()

            if city:
                reply = get_weather(city)
            else:
                reply = "Please tell me the city name."

        # Battery

        elif user_input in ["battery", "battery percentage"]:
            reply = get_battery()

        # Screenshot

        elif user_input in ["screenshot", "take screenshot"]:
            reply = take_screenshot()

        # ---------- System Commands ----------

        elif user_input == "open notepad":
            open_notepad()
            reply = "Opening Notepad"

        elif user_input == "open calculator":
            open_calculator()
            reply = "Opening Calculator"

        elif user_input == "open paint":
            open_paint()
            reply = "Opening Paint"

        elif user_input == "open cmd":
            open_cmd()
            reply = "Opening Command Prompt"

        elif user_input == "open explorer":
            open_explorer()
            reply = "Opening File Explorer"

        elif user_input == "open downloads":
            open_downloads()
            reply = "Opening Downloads Folder"

        # ---------- Web Commands ----------

        elif user_input == "open google":
            open_google()
            reply = "Opening Google"

        elif user_input == "open youtube":
            open_youtube()
            reply = "Opening YouTube"

        elif user_input == "open github":
            open_github()
            reply = "Opening GitHub"

        elif user_input == "open gmail":
            open_gmail()
            reply = "Opening Gmail"

        elif user_input.startswith("search google"):
            query = user_input.replace("search google", "").strip()

            if query:
                search_google(query)
                reply = f"Searching Google for {query}"
            else:
                reply = "Please tell me what to search."

        elif user_input.startswith("search youtube"):
            query = user_input.replace("search youtube", "").strip()

            if query:
                search_youtube(query)
                reply = f"Searching YouTube for {query}"
            else:
                reply = "Please tell me what to search."

        # AI

        else:
            reply = chat_with_ai(user_input)

        print(f"{ASSISTANT_NAME}: {reply}")
        asyncio.run(speak(reply))


if __name__ == "__main__":
    main()