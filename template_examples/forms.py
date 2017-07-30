from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired, EqualTo, Required


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=20)])
    email = StringField('Email Address', validators=[Length(min=6, max=50)])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        EqualTo('confirm', message='Password must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice',
                              validators=[Required])
