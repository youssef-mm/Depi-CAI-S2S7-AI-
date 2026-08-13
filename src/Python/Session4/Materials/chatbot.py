'''
This is a simple chatbot program that responds to user input based on predefined responses. The chatbot can recognize greetings, inquiries about its well-being, and farewells. If the user input does not match any of the predefined categories, the chatbot will provide a default response indicating that it did not understand the input.

'''

import random

responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
}
 
def get_responses(user_input):
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return random.choice(responses["default"])  