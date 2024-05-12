from flask import Flask
from dotenv import load_dotenv
import os
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "database.db"

load_dotenv()
secret = os.getenv("SESSION_COOKIE_SECRET")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # Registering the blueprints
    app.register_blueprint(views, url_prefix="/")  # /views/
    app.register_blueprint(auth, url_prefix="/")  # /auth/

    return app
