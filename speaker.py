from config import VOICE
import asyncio
import edge_tts
import pygame
import os


async def speak(text):
    # Agar purani file hai to delete karo
    if os.path.exists("voice.mp3"):
        try:
            os.remove("voice.mp3")
        except PermissionError:
            pass

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()


if __name__ == "__main__":
    asyncio.run(speak("Hello Armaan! I am Vaani AI."))