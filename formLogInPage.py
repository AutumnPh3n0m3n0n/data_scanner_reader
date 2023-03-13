from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired(), validators.Length(min=2, max=30)])
    email = EmailField("Email", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired(),
                                          validators.EqualTo("confirm_password", message="Passwords must match")])
    confirm_password = PasswordField('Repeat Password')
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
