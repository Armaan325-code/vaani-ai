# import asyncio
# import edge_tts

# text= "hello Armaan ! i am vaani ai"
# async def speak():
#     communication = edge_tts.communicate(
#         text,
#         voice= "hi-IN-SwaraNaural"
#     )
#     await communicate.save("voice.mp3")

# asyncio.run(speak())

# import pygame

# pygame.mixer.init()
# pygame.mixer.music.load("voice.mp3")
# pygame.mixer.music.play()

# while pygame.mixer.music.get_busy():
#     pass

# import asyncio
# import edge_tts

# text = "Hello Armaan! I am Vaani AI."

# async def speak():
#     communication = edge_tts.Communicate(
#         text,
#         voice="hi-IN-SwaraNeural"
#     )

#     await communication.save("voice.mp3")

# asyncio.run(speak())

import asyncio
import edge_tts

VOICE = "hi-IN-SwaraNeural"

async def speak(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("voice.mp3")
    print("Voice file created successfully!")

if __name__ == "__main__":
    asyncio.run(speak("Hello Armaan AND JASSI! I am Vaani AI."))