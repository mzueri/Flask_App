from flask import Blueprint, render_template, request, session, redirect, url_for
from app.extensions import db
from app.models.users import User


auth_bp = Blueprint("auth", __name__)



@auth_bp.route("/login/", methods=["GET", "POST"])
def login():

    if request.method=="POST":
        input_username=request.form.get("username")
        input_password=request.form.get("password")

        try:
            user=db.session.execute(db.select(User).filter_by(username=input_username)).scalar_one()
            if user.password==input_password:
                session["user"]={"id":user.id,"username":input_username}
                return redirect(url_for("main.home"))
            else:
                return 'Invalid password. <a href="/login">Try again</a> or create an account <a href="/register">Create an account</a>. <a href="/">Home</a>'
        except:
            return 'User does not exist. <a href="/login">Try again</a> or create an account <a href="/register">Create an account</a>. <a href="/">Home</a>'

    return render_template("login.html")



@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            user = User(username=username,password=password)
            db.session.add(user)
            db.session.commit()
        except:
            return 'Username already exists. <a href="/register">Try again</a>. <a href="/">Home</a>'

        session['user'] = {"id":user.id,"username":username}
        return redirect(url_for("main.home"))
    
    return render_template("register.html")



@auth_bp.route("/logout/")
def logout():
    session.pop("user", None) # removes the user from the session. 
    # session.clear()  # Uncomment this to remove all session data, terminating the session.
    return redirect(url_for("main.home"))
