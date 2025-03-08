from flask import Blueprint, render_template, request, session, redirect, url_for

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login/", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        session["username"]=request.form.get("username")
        session["password"]=request.form.get("password")
        return redirect(url_for("main.home"))
    return render_template("login.html")

@auth_bp.route("/logout/")
def logout():
    session.pop('username', None) # removes the username from the session. 
    # session.clear()  # Uncomment this to remove all session data, terminating the session.
    return redirect(url_for("main.home"))
