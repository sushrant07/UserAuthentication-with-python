from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class Signup(FlaskForm):
    email = StringField('Email:',validators=[DataRequired(),Email()])
    password = PasswordField("  PassWord :", validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password=PasswordField("Confirm Password", validators=[DataRequired()])
    # phoneno = StringField("Phone Number:")
    signup = SubmitField("Sign Up")


class Login(FlaskForm):
    email = StringField("Email:",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    login = SubmitField("Log In")

class DelForm(FlaskForm):
	id = StringField("Id to Delete?")
	submit = SubmitField("Really want to delete")
