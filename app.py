from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("test")
def test():
    return render_template("index.html")


def chad():
    return "hello"