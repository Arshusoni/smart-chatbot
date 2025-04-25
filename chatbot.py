# chatbot.py
import json
import os
import requests

DATA_FILE = "data.json"

# Load memory from file or create new
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        faq = json.load(file)
else:
<<<<<<< HEAD
    faq = {}

# Save memory to file
=======

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
    
>>>>>>> f591a1a46ee850ff3e11ceaa117964debfcf9a9c
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(faq, file, indent=4)

# Get response from memory or Ollama
def get_response(user_input):
    user_input = user_input.lower()

    # Learn new answer
    if user_input.startswith("answer:"):
        try:
            question = user_input.split("|")[1].strip()
            answer = user_input.split("answer:")[1].split("|")[0].strip()
            faq[question] = answer
            save_data()
            return "Thanks! I’ve learned something new."
        except:
            return "Incorrect format. Use: answer: your answer | your question"

    # Check learned memory
    for question in faq:
        if question in user_input:
            return faq[question]

    # Fallback to Ollama
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama2:latest",
            "prompt": user_input,
            "stream": False
        })
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
