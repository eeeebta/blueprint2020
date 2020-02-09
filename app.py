from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, jsonify
import spotipy
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

