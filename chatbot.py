# chatbot.py

def get_response(user_input):

    responses = {
        "where is food court": "The food court is on the third floor.",
        "where is washroom": "Washroom is near the elevator.",
        "hello": "Hello! Welcome to Smart Mall."
    }

    user_input = user_input.lower()

    return responses.get(user_input, "Sorry, I don't understand.")


# Test
user = input("Ask: ")
reply = get_response(user)

print(reply)
