from flask import Flask, render_template, request, redirect, url_for,session
import webbrowser
import threading
import asyncio
import sqlite3

from speaker import speak
from main import process_message

app = Flask(__name__)
app.secret_key = "vaani_ai_secret_key"


# Login Page
@app.route("/")
def home():
    return render_template(
        "login.html"
    )


# Signup Page
@app.route("/signup")
def signup():
    return render_template("signup.html")


# Signup User
@app.route("/signup_user", methods=["POST"])
def signup_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("vaani.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

    except sqlite3.IntegrityError:
        conn.close()
        return "Username already exists!"

    conn.close()

    return redirect(url_for("home"))
#login users
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("vaani.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        session["username"] = username
        return render_template(
        "dashboard.html",
        chats=get_chats()
    )


    return "Invalid Username or Password!"
#new chat buton

@app.route("/new_chat")
def new_chat():
    return render_template(
        "dashboard.html",
        chats=get_chats()
    )
@app.route("/logout")
def logout():
    return redirect(url_for("home"))

# Chat
def get_chats():

    if "username" not in session:
        return[]

    conn = sqlite3.connect("vaani.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_message
        FROM chats
        WHERE username=?
        ORDER BY id desc           
    """,
    (session["username"],)
    )

    chats = cursor.fetchall()

    conn.close()

    return chats


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.form["message"]

    reply = process_message(user_message)

    conn = sqlite3.connect("vaani.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats(username, user_message, ai_reply) VALUES (?, ?, ?)",
        (session["username"], user_message, reply)
    )

    conn.commit()
    conn.close()

    asyncio.run(speak(reply))

    return render_template(
        "dashboard.html",
        user_message=user_message,
        reply=reply,
        chats=get_chats()
    )

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)