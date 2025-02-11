# make sure the third party library "flask" is installed (otherwise use "pip install Flask"). 
# use "flask run" in the terminal to run this app on your localserver and display in the browser.

from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session # for server-side sessions
from datetime import timedelta

app = Flask(__name__) # turn this file into a Flask application.


app.secret_key = 'top_secret_key_007' # Secret key for session encryption
app.config['SESSION_TYPE'] = 'filesystem' # Store session data in a local file
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2) # Set timeout to 2 mins
app.config['SESSION_FILE_DIR'] = './flask_sessions'  # Custom folder for session files
Session(app) # Initialize session on server-side


# Dummy user database (replace with a real database)
users = {
    "admin": "password123",
    "user1": "mypassword"
}


@app.route("/") 
def home():
    if "username" in session: 
        return render_template("home.html",username=session["username"])
    return render_template("home.html",username=None)

@app.route("/login/", methods=["GET","POST"]) 
def login():
    if request.method=="POST":
        session["username"]=request.form.get("username")
        session["password"]=request.form.get("password")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout/") 
def logout():
    session.pop('username', None) # removes the username from the session. 
    # session.clear()  # Uncomment this to remove all session data, terminating the session.
    return redirect(url_for("home"))



@app.route("/hello/") # here is code that I want the server to execute. 
def hello_world():
    #return "hello world"
    return render_template("hello_world.html") # the render_template function goes into templates folder and searches for the file "index.html", will open it up and spit it out to the browser.

@app.route("/greet/", methods=["GET","POST"]) 
def greet():
    if request.method=="POST": # for the sake of privacy we use not a GET request (we do not want the input to appear in the URL).
        name=request.form.get("name") # note that for "POST" we need request.form instead of request.args as for "GET".
    else:
        name=None
    return render_template("greet.html", name=name) 
