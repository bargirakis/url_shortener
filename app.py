from flask import Flask, url_for
from flask_migrate import Migrate
from markupsafe import escape
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from db import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return f"hello world - to be greeted, visit {url_for('hello', name = 'greeting')}"

@app.route("/hello/<path:name>")
def hello(name):
    return f'hello {escape(name)}'