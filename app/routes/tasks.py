from flask import Blueprint, render_template, request, session

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/taskmanager/")
def taskmanager():
    if "task_list" not in session:
        session["task_list"]=[]
    return render_template("taskmanager.html",task_list=session["task_list"])



@tasks_bp.route("/add_task/", methods=["GET", "POST"])
def add_task():
    if request.method=="POST": 
        new_task = {
            "Task": request.form.get("task"), 
            "Deadline": request.form.get("deadline"),
            "Priority": request.form.get("priority")
            }
        session["task_list"].append(new_task)
        return render_template("taskmanager.html",task_list=session["task_list"])
    return render_template("add_task.html")



@tasks_bp.route("/delete_task/", methods=["POST"])
def delete_task():
    pass
    return render_template("taskmanager.html",task_list=session["task_list"])

