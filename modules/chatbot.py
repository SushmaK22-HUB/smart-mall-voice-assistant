import google.generativeai as genai

# Your working Gemini API Key
GEMINI_API_KEY = "AIzaSyAPY-iiz7pSvOEDDMTIyH4VEKGuyBASHSE"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def get_response(user_input):

    try:
        response = model.generate_content(user_input)

        return response.text

    except Exception as e:
        return f"Error: {e}"


# Chatbot Testing
if __name__ == "__main__":

    print("🛍️ Smart Mall AI Assistant Started")
    print("Type 'exit' to stop\n")

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            print("Assistant: Thank you for visiting Smart Mall")
            break

        answer = get_response(user)

        print("\nAssistant:", answer)
        print()