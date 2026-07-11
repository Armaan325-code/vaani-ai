from flask import Flask, render_template, request
import webbrowser
import threading

from chatbot import chat_with_ai

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.form["message"]

    reply = chat_with_ai(user_message)

    return render_template(
        "index.html",
        user_message=user_message,
        reply=reply
    )


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)