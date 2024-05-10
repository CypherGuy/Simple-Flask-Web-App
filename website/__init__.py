from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
secret = os.getenv("SESSION_COOKIE_SECRET")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret

    return app
