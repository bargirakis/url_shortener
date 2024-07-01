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

class Url(db.Model):

    __tablename__ = "url"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str] = mapped_column(String(5))
    long_url: Mapped[str] = mapped_column(String(2000))
    created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now(datetime.UTC))

    def __repr__(self) -> str:
        return f"URL(id={self.id!r}, short_url={self.short_url!r}, long_url={self.long_url!r})"

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return f"hello world - to be greeted, visit {url_for('hello', name = 'greeting')}"

@app.route("/hello/<path:name>")
def hello(name):
    return f'hello {escape(name)}'