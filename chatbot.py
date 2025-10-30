def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBuddy, your virtual assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure I understand. Can you say that differently?"


