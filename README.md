# Flask_App

To run the app instance follow the following steps: 

pip install -r requirements.txt.
set secrets in a JSON file called "secrets.json".
If not already done set up the database (run setup.py).
Run 'python run.py' in the terminal.

To run the docker container:
First, build the Docker image: docker build -t my-flask_app .
Then you can run it: docker run -p 127.0.0.1:5000:5000 my-flask-app
