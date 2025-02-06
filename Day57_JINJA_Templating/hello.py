from flask import Flask,render_template
import random
import requests
from datetime import datetime
today=datetime.now()

app=Flask(__name__)

@app.route("/")
def hello():
    randomNumber=random.randint(1,10)
    today_year=today.year
    return render_template("index.html",num=randomNumber,year=today_year)

# exercise:
@app.route("/guess/<name>")
def exercise(name):
    today_year=today.year

    genderize_response=requests.get(url=f"https://api.genderize.io?name={name}")
    print(genderize_response.json())
    expected_gender=genderize_response.json()["gender"]

    agify_response=requests.get(url=f"https://api.agify.io?name={name}")
    print(agify_response.json())
    expected_age=agify_response.json()["age"]

    return render_template("index2.html",year=today_year,user_name=name.title(),gender=expected_gender,age=expected_age)

@app.route("/blog")
def getBlog():
    blog_response=requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_data=blog_response.json()
    return render_template("blog.html",allPosts=blog_data)

@app.route("/post/<int:postId>")
def getPost(postId):
    post_requested=None
    blog_response=requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_data=blog_response.json()
    for post in blog_data:
        if post["id"]==postId:
            post_requested=post
    return render_template("post.html",sendPost=post_requested)

if __name__=="__main__":
    app.run(debug=True)