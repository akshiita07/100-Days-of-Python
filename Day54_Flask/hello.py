# pip install Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")     #decorator function: ie run hello_world function only when route is /
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_world():
    return "<p>Goodbye</p>"

# to run file: flask --app hello run
if __name__=="__main__":
    app.run()
