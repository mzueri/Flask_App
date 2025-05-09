from flask import Blueprint, render_template, request, session
from app.routes.quotes import quotes
import random
from datetime import date

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():

    # pick a random quote every other day.
    today = date.today().toordinal()  # Converts to a number: days since year 1
    random.seed(today)  # Set seed based on date
    daily_quote = random.choice(quotes)

    if "user" in session:
        return render_template("home.html", signed_in=True, daily_quote=daily_quote)
    else:
        return render_template("home.html",signed_in=False, daily_quote=daily_quote)

@main_bp.route("/hello/")
def hello_world():
    #return "hello world"
    return render_template("hello_world.html") # the render_template function goes into templates folder and searches for the file "index.html", will open it up and spit it out to the browser.

@main_bp.route("/greet/", methods=["GET", "POST"])
def greet():
    if request.method=="POST": # for the sake of privacy we use not a GET request (we do not want the input to appear in the URL).
        name=request.form.get("name") # note that for "POST" we need request.form instead of request.args as for "GET".
    else:
        name=None
    return render_template("greet.html", name=name) 
