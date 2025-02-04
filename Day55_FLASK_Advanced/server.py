from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="200" height="200"/>'

@app.route("/<int:number>")
def checkNum(number):
    if number<5:
        return '<h1 style="color:red">Too low! Try again.</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="200" height="200"/>'
    elif number>8:
        return '<h1 style="color:purple">Too high! Try again.</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="200" height="200"/>'
    else:
        return '<h1 style="color:green">You found me!!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="200" height="200"/>'

if __name__=="__main__":
    app.run(debug=True)