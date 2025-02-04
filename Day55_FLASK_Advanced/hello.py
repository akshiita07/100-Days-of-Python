from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<b><em><u>Hello, World!</u></em></b>"
# b:bold em:italics u:underline

@app.route("/bye")
def bye_world():
    return "<em>Goodbye</em>"

# ADDING VARIABLE NAME IN URL:
@app.route("/username/<name>/<int:age>")
def greet(name,age):
    return f"Hello {name}! You are {age} years old."

@app.route("/test/<path:name>")     #it will take input as full path
def testing(name):
    return f"Hello {name}!"

@app.route("/html")     #it will take input as full path
def renderHtml():
    return '<h1 style="text-align:center">Hello World</h1>'\
            '<p style="color:red">This is a paragraph</p>'\
            '<a href="https://leetcode.com/akshitapathak">Visit here!</a>'\
            '<ul>'\
            '<li>This is item 1</li>'\
            '<li>This is item 2</li>'\
            '</ul>'\
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjRraWt5YTdoamN2Zm55Ynk4bDI0b2s4azE2c2d3Y2Q3czJwaGg4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8lw0B6senWhFZ7nMds/giphy.gif" width="300" height="300"/>'        #https://giphy.com/

# defining decorators:
def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

def make_italics(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

@app.route("/decorators")
@make_bold
@make_underline
@make_italics
def decorate():
    return "Lets learn python decorators"

if __name__=="__main__":
    app.run(debug=True)
