from flask import Blueprint, render_template, request, session
import pandas as pd

tasks_bp = Blueprint("tasks", __name__)




@tasks_bp.route("/taskmanager/")
def taskmanager():
    if "df_tasks" in session: 
        return render_template("taskmanager.html",df_tasks=session["df_tasks"], is_empty=session["df_tasks"].empty)
    return render_template("taskmanager.html",df_tasks=pd.DataFrame(), is_empty=True)

@tasks_bp.route("/add_task/", methods=["GET", "POST"])
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
