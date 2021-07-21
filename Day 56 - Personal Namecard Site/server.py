from flask import Flask, render_template
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
# render_template imports HTML files from the "templates" directory folder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)