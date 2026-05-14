# chatbot.py

import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# AI Response Function
def get_response(user_input):

    user_input = user_input.lower()

    # Smart Mall Responses
    if "food court" in user_input:
        return "The food court is located on the third floor."

    elif "washroom" in user_input:
        return "The washroom is near the elevator."

    elif "parking" in user_input:
        return "Parking is available in basement level one."

    elif "lift" in user_input or "elevator" in user_input:
        return "The elevator is beside the main entrance."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to Smart Mall."

    elif "exit" in user_input or "bye" in user_input:
        return "Thank you for visiting Smart Mall."

    else:
        return "Sorry, I could not understand your question."


# MAIN PROGRAM
print("AI Smart Mall Assistant Started")
print("Type 'exit' to stop")

while True:

    user = input("\nYou: ")

    response = get_response(user)

    print("Assistant:", response)

    speak(response)

    if user.lower() == "exit":
        break
