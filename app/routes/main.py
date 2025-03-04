from flask import Blueprint, render_template, request, session
import pandas as pd

main_bp = Blueprint("main", __name__)



@main_bp.route("/")
def home():
    if "username" in session: 
        return render_template("home.html",username=session["username"])
    return render_template("home.html",username=None)

@main_bp.route("/taskmanager/")
def taskmanager():
    if "df_tasks" in session: 
        return render_template("taskmanager.html",df_tasks=session["df_tasks"], is_empty=session["df_tasks"].empty)
    return render_template("taskmanager.html",df_tasks=pd.DataFrame(), is_empty=True)

@main_bp.route("/add_task/", methods=["GET", "POST"])
def add_task():
    if request.method=="POST": 
        df_new_task = pd.DataFrame([{"tasks": request.form.get("task"), 
                                      "deadline": request.form.get("deadline"), 
                                      "priority": request.form.get("priority")}])
        if "df_tasks" not in session:
            session["df_tasks"]=df_new_task
        else:
            session["df_tasks"] = pd.concat([session["df_tasks"], df_new_task], ignore_index=True)
        return render_template("taskmanager.html",df_tasks=session["df_tasks"])
    return render_template("add_task.html")

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
