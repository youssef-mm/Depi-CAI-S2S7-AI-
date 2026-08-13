from chatbot import get_responses

def main():
    print("chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = get_responses(user_input)
        print("chatbot:", response)

        if user_input.lower() == "goodbye":
            break

main()