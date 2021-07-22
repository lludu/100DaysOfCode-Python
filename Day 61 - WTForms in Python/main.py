from flask import Flask, render_template, request
# Flask Quickstart: https://flask.palletsprojects.com/en/2.0.x/quickstart/

# WTForms Documentation: https://flask-wtf.readthedocs.io/en/0.15.x/
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask_bootstrap import Bootstrap
# Flask Bootstrap documentation: https://pythonhosted.org/Flask-Bootstrap/basic-usage.html



class LoginForm(FlaskForm):
    # https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators

    email = StringField(label='Email', validators=[DataRequired(), Email()])  #This is the label property in use in login.html when our form object is passed over.
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])  #This is the label property in use in login.html when our form object is passed over.
    submit = SubmitField(label="Log In")


# import smtplib
# import requests
# from p_data import *

app = Flask(__name__)
app.secret_key = "poptarts"  # Key for the flask form (LoginForm)  # any-string-you-want-just-keep-it-secret
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)