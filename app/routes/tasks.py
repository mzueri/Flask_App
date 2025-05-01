from flask import Blueprint, render_template, request, session
from app.cache_storage import cache_tasks_db

tasks_bp = Blueprint("tasks", __name__)



task_cols=["Task","Deadline","Priority"]

@tasks_bp.route("/taskmanager/")
def taskmanager():
    if "username" not in session:
        return 'You need to sign in first. User <a href="/register">Sign up</a> to create an account or <a href="/login">Login</a> to use a existing account.'
    if "task_list" not in session:
        session["task_list"]=[]
    return render_template("taskmanager.html",task_list=session["task_list"],task_cols=task_cols)



@tasks_bp.route("/add_task/", methods=["GET", "POST"])
def add_task():
    if request.method=="POST": 
        new_task = {
            "Task": request.form.get("task"), 
            "Deadline": request.form.get("deadline"),
            "Priority": request.form.get("priority")
            }
        assert list(new_task.keys())==task_cols, "Correct the task columns accordingly."
        session["task_list"].append(new_task)
        return render_template("taskmanager.html",task_list=session["task_list"],task_cols=task_cols)
    return render_template("add_task.html")



@tasks_bp.route("/delete_task/", methods=["POST"])
def delete_task():
    row_index=int(request.form.get("row_index"))
    session["task_list"].pop(row_index)
    return render_template("taskmanager.html",task_list=session["task_list"],task_cols=task_cols)

