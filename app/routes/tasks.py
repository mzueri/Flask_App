from flask import Blueprint, render_template, request, session
from app.extensions import db
from app.models.tasks import Task
from datetime import datetime

tasks_bp = Blueprint("tasks", __name__)


task_cols=["task","deadline","priority"]

@tasks_bp.route("/taskmanager/")
def taskmanager():
    
    if "user" not in session:
        return render_template("please_login.html")
    
    task_list=db.session.execute(db.select(Task).filter_by(user_id=session["user"]["id"])).scalars().all()
        
    return render_template("taskmanager.html",task_list=task_list,task_cols=task_cols,signed_in=True)



@tasks_bp.route("/add_task/", methods=["GET", "POST"])
def add_task():

    if "user" not in session:
        return render_template("please_login.html")

    if request.method=="POST": 
        # add the added task to the db.
        new_task = Task(user_id=session["user"]["id"],
                        task=request.form.get("task"),
                        deadline=request.form.get("deadline"),
                        priority=request.form.get("priority"))
        db.session.add(new_task)
        db.session.commit()
        
        task_list=db.session.execute(db.select(Task).filter_by(user_id=session["user"]["id"])).scalars().all()

        return render_template("taskmanager.html",task_list=task_list,task_cols=task_cols,signed_in=True)
    
    return render_template("add_task.html",signed_in=True)



@tasks_bp.route("/delete_task/", methods=["POST"])
def delete_task():

    if "user" not in session:
        return render_template("please_login.html")

    task_id=int(request.form.get("task_id"))
    
    # delete the task with the above id from the db.
    task_to_delete=db.session.execute(db.select(Task).filter_by(id=task_id)).scalar_one()
    db.session.delete(task_to_delete)
    db.session.commit()

    task_list=db.session.execute(db.select(Task).filter_by(user_id=session["user"]["id"])).scalars().all()
        
    return render_template("taskmanager.html",task_list=task_list,task_cols=task_cols,signed_in=True)
