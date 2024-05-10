from flask import Flask
from dotenv import load_dotenv
import os
from .views import views
from .auth import auth

load_dotenv()
secret = os.getenv("SESSION_COOKIE_SECRET")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret

    # Registering the blueprints
    app.register_blueprint(views, url_prefix="/")  # /views/
    app.register_blueprint(auth, url_prefix="/")  # /auth/

    return app
