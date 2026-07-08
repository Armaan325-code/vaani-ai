import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")

        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=3)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            text = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You:", text)
            return text

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""

        except sr.RequestError as e:
            print("Speech Recognition Error:", e)
            return ""

        except Exception as e:
            print("Error:", e)
            return ""