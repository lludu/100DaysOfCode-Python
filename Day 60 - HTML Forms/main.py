from flask import Flask, render_template, request
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
# render_template imports HTML files from the "templates" directory folder
import smtplib
import requests
from p_data import *

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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == '__main__':
    app.run(debug=True)