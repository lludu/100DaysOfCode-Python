from flask import Flask, render_template
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
# render_template imports HTML files from the "templates" directory folder

import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    CURRENT_YEAR = datetime.datetime.today().year
    return render_template("index.html", num = random_number, year = CURRENT_YEAR)

@app.route('/guess/<name>')
def guess_name(name):
    name = name.capitalize()

    response = requests.get(url=f'https://api.genderize.io?name={name}')
    data = response.json()
    gender = data['gender'].capitalize()

    response = requests.get(url=f'https://api.agify.io?name={name}')
    data = response.json()
    age = data['age']

    return render_template("name_guess.html", name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/ed99320662742443cc5b'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)