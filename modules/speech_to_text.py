import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Calibrating ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            print("Listening for speech...")
            # Timeout: waits 4 seconds for speech to begin; phrase limit: 6 seconds of speaking
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=6)

        text = recognizer.recognize_google(audio)
        return text
    except sr.WaitTimeoutError:
        return "Listening timed out. No speech detected."
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError:
        return "Speech service unavailable. Please check internet connection."
    except Exception as e:
        return f"Microphone error: {e}"


if __name__ == "__main__":
    print("Testing speech recognition (say something)...")
    result = listen()
    print("You said:", result)