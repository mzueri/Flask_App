from flask import Blueprint, render_template, request, session

main_bp = Blueprint("main", __name__)



@main_bp.route("/")
def home():
    if "username" in session: 
        return render_template("home.html",username=session["username"])
    return render_template("home.html",username=None)

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
