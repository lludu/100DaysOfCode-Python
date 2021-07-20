from flask import Flask
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Goodbye!'

@app.route('/portfolio')
def portfolio_link():
    return '<a href="http://www.andrewjash.com">Andrew Portfolio</a>'




# ----------- Start Flask Server without Terminal ----------------- #
# print(__name__)
if __name__ == "__main__":
    app.run()

# ----------- Start Flask Server with Hyper/Bash Terminal ----------------- #
# export FLASK_APP=hello.py
# flask run
