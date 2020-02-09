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