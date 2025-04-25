# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__, static_folder='./static/')

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
