def chatbot():
    print("Chatbot: Hello! How can I help you today? (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello there!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing fine!")
        elif 'your name' in user_input:
            print("Chatbot: I'm a rule-based chatbot created by Anshika.")
        elif 'bye' in user_input or 'exit' in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()