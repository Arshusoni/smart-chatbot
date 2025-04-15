import json
import os

DATA_FILE = "data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        faq = json.load(file)
else:
    faq = {
        "how to check my balance": "You can check your balance by dialing *123#.",
        "how to recharge my number": "Use our app or dial *456# to recharge.",
        "how to talk to customer care": "Call 198 to speak to customer care.",
        "what are the latest plans": "Visit our website or app to explore new plans.",
    }

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(faq, file, indent=4)

def get_response(user_input):
    user_input = user_input.lower()

    if user_input.startswith("answer:"):
        question = user_input.split("|")[1]
        answer = user_input.split("answer:")[1].split("|")[0]
        faq[question] = answer
        save_data()
        return "Thanks! I’ve learned something new."

    for question in faq:
        if question in user_input:
            return faq[question]

    return "I don't know the answer to that. Type 'answer: your answer here | original question' to teach me!"
