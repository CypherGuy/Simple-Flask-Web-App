# Stores authy routes for the website

from flask import Blueprint, render_template, request, flash
auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if len(email) < 6:
            flash("Email must be greater than 6 characters", category="error")
        elif len(username) < 2:
            flash("Username must be greater than 2 characters", category="error")
        elif len(password) < 6:
            flash("Password must be greater than 6 characters", category="error")
        elif password != confirmation:
            flash("Passwords do not match", category="error")
        else:
            flash("Success", category="success")
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"
