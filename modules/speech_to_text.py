import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        return text

    except:

        return "Sorry, could not understand."


# Testing the module
if __name__ == "__main__":

    result = listen()

    print("You said:", result)