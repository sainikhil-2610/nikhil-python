responses = {
    "hello": "Hi!",
    "how are you": "I'm good, thanks!",
    "what's your name": "I'm a chatbot!"
}
while True:
    user_input = input("You: ")
    print("Chatbot:", responses.get(user_input.lower(), "I didn't understand that!"))