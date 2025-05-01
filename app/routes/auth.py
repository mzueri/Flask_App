from flask import Blueprint, render_template, request, session, redirect, url_for
from app.cache_storage import cache_users_db

auth_bp = Blueprint("auth", __name__)



@auth_bp.route("/login/", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        input_username=request.form.get("username")
        input_password=request.form.get("password")
        if input_username in cache_users_db and cache_users_db[input_username]==input_password:
            session["username"] = input_username
            return redirect(url_for("main.home"))
        else:
            return 'Invalid credentials. <a href="/login">Try again</a> or create an account <a href="/register">Create an account</a>. <a href="/">Home</a>'
    return render_template("login.html")


@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in cache_users_db:
            return 'Username already exists. <a href="/register">Try again</a>. <a href="/">Home</a>'
        cache_users_db[username] = password
        session['username'] = username
        return redirect(url_for("main.home"))
    
    return render_template("register.html")

@auth_bp.route("/logout/")
def logout():
    session.pop('username', None) # removes the username from the session. 
    # session.clear()  # Uncomment this to remove all session data, terminating the session.
    return redirect(url_for("main.home"))
