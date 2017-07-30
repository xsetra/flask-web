from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired, EqualTo


class RegistrationForm(Form):
    username = StringField('Username', validators=Length(min=4, max=20))
    email = StringField('Email Address', validators=Length(min=6, max=50))
    password = PasswordField('New Password', validators=[
        DataRequired(),
        EqualTo('confirm', message='Password must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              validators=DataRequired())
