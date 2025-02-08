from flask import Flask, render_template, request

app = Flask(__name__) # turn this file into a Flask application.

@app.route("/") # here is code that I want the server to execute. 
def index():
    #return "hello world"
    return render_template("index.html") # the render_template function goes into templates folder and searches for the file "index.html", will open it up and spit it out to the browser.

# make sure the third party library "flask" is installed (otherwise use "pip install Flask"). 
# use "flask run" in the terminal to run this app on your localserver and display in the browser.