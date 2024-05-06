from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"hello world - to be greeted, visit {url_for('hello', name = 'greeting')}"

@app.route("/hello/<path:name>")
def hello(name):
    return f'hello {escape(name)}'