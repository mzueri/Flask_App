# make sure the third party library "flask" is installed (otherwise use "pip install Flask"). 
# use "flask run" in the terminal to run this app on your localserver and display in the browser.

from flask import Flask, render_template, request

app = Flask(__name__) # turn this file into a Flask application.

@app.route("/hello/") # here is code that I want the server to execute. 
def hello_world():
    #return "hello world"
    return render_template("hello_world.html") # the render_template function goes into templates folder and searches for the file "index.html", will open it up and spit it out to the browser.

@app.route("/", methods=["GET","POST"]) 
def index():
    if request.method == "GET":
        return render_template("index.html") 
    elif request.method == "POST": # for the sake of privacy we use not a GET request (we do not want the input to appear in the URL).
        return render_template("greet.html", name=request.form.get("name")) 
        # note that for "POST" we need request.form instead of request.args as for "GET".