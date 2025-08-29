from flask_wtf import FlaskForm
from wtforms.fields.choices import RadioField, SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField, TextAreaField, BooleanField, SubmitField


class MyForm(FlaskForm):
    username = StringField('Username')      #Label Field username
    password = PasswordField('Password')    #Label Field Password
    email = StringField('Email')
    bio = TextAreaField('Bio')
    phone = IntegerField("Phone Number")
    gender = RadioField("Gender",choices=[('male','Male'),('female','Female')])
    course = SelectField("Course",choices=[('Java','java'),('Python','python'),('Others','others')])
    birthdate = DateField("Date-Of-Birth",format='%Y-%m-%d')
    subscribe = BooleanField("Subscribe")
    submit = SubmitField("Submit")

