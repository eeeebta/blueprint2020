from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blueprint")
def blueprint():
    tweets = []
    with open("valid_links.txt", "r") as grabbed_tweets:
        for tweet in grabbed_tweets:
            tweets.append(tweet)
    return render_template("blueprint.html", tweets=tweets)
