import random

def chatbot():
    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple bot created to assist you.",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I didn't understand that. Can you rephrase?"
    }

    print("chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("chatbot: Goodbye! Have a nice day!")
            break

        response = responses.get(user_input, responses["default"])
        print(f"chatbot: {response}")

if __name__ == "__main__":
    chatbot()