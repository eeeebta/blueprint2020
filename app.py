from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, jsonify
import spotipy
app = Flask(__name__)


# Quiz at start or separate?
# Index -> quiz?
@app.route("/")
def index():
    return render_template("index.html")


# If different
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/make")
def create_playlist():
    return render_template("make.html")


# Channels {Thread: {message data}}
channels = {"id": {"General": {"message": ["date and time pushed"]}}}


@app.route("/chat", methods=["GET", "POST"])
def chat_room():

    if request.method == "GET":
        # Grab initial page with channels
        return render_template("chat.html", posts=channels)
    else:
        return render_template("chat.html", )


@app.route("/form/<grabbed_id>", methods=["GET"])
def thread(grabbed_id):
    if grabbed_id not in channels:
        return render_template("error.html")

# Database stuff
# https://www.youtube.com/watch?v=cYWiDiIUxQc
