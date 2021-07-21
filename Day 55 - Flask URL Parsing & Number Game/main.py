from flask import Flask
# Flask Quickstart = https://flask.palletsprojects.com/en/2.0.x/quickstart/
# from markupsafe import escape
app = Flask(__name__)


# make_bold
def make_bold(function):
    """Decorator function that adds <b> tags to any returned output"""
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

# make_em
def make_emphasis(function):
    """Decorator function that adds <em> tags to any returned output"""
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

# make_underline
def make_underlined(function):
    """Decorator function that adds <u> tags to any returned output"""
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Goodbye!'

@app.route('/<name>')
def show_user_profile(name):
    return f'User {name}'


@app.route('/portfolio')
def portfolio_link():
    return '<a href="http://www.andrewjash.com">Andrew Portfolio</a>'




# ----------- Start Flask Server without Terminal ----------------- #
# print(__name__)
if __name__ == "__main__":
    app.run(debug=True)

# ----------- Start Flask Server with Hyper/Bash Terminal ----------------- #
# export FLASK_APP=hello.py
# flask run
