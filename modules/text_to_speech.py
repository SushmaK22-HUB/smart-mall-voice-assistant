import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """
    Convert assistant response to speech.
    """
    engine.say(text)
    engine.runAndWait()


# Example integration
if __name__ == "__main__":

    assistant_response = (
        "Welcome to Smart Mall. Nike store is located on the second floor near the main entrance."
    )

    print("Assistant:", assistant_response)

    # Convert response to audio
    speak(assistant_response)