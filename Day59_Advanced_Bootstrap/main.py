from flask import Flask,render_template
app=Flask(__name__)

api_endpoint="https://www.npoint.io/docs/f8d4f73962baf49d031d"


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def hello1():
    return render_template('about.html')

@app.route("/contact")
def hello2():
    return render_template('contact.html')

@app.route("/post")
def hello3():
    return render_template('post.html')

if __name__=="__main__":
    app.run(debug=True)