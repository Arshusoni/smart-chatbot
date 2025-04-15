import json
import os

DATA_FILE = "data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        faq = json.load(file)
else:

 import requests

def get_response(user_input):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama2",
        "prompt": user_input,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
    
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
