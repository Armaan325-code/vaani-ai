import pyautogui
from datetime import datetime
import os


def take_screenshot():
    folder = "screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    filepath = os.path.join(folder, filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)

    return f"Screenshot saved successfully as {filename}"