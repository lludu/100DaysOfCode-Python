from flask import Flask, render_template
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
# render_template imports HTML files from the "templates" directory folder

import requests

posts = requests.get("https://gist.githubusercontent.com/lludu/3b42570ff4b44464e270f586ccbb8305/raw/d3c127eae8436a265314f637f30a249a43695690/data.json").json()

app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)