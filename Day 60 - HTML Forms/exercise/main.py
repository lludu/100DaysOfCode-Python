from flask import Flask, render_template, request
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
# render_template imports HTML files from the "templates" directory folder
import requests



app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"



if __name__ == '__main__':
    app.run(debug=True)