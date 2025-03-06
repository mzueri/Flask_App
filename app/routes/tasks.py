from flask import Blueprint, render_template, request, session
import pandas as pd

tasks_bp = Blueprint("tasks", __name__)




@tasks_bp.route("/taskmanager/")
def taskmanager():
    if "dict_tasks" not in session:
        session["dict_tasks"]={}
    return render_template("taskmanager.html",dict_tasks=session["dict_tasks"])

@tasks_bp.route("/add_task/", methods=["GET", "POST"])
def add_task():
    if request.method=="POST": 
        new_task = {"Task": [request.form.get("task")], 
                                      "Deadline": [request.form.get("deadline")], 
                                      "Priority": [request.form.get("priority")]}
        dict_tasks=session["dict_tasks"]
        if session["dict_tasks"]:
            session["dict_tasks"] = {key: dict_tasks.get(key) + new_task.get(key) for key in set(dict_tasks) | set(new_task)}
        else:
            session["dict_tasks"]=new_task
        return render_template("taskmanager.html",dict_tasks=session["dict_tasks"])
    return render_template("add_task.html")
