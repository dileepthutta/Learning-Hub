from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Enter a valid email address")
        ]
    )

    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message="Password is required"),
            Length(min=8, message="Password must be 8 letters.")
        ]
    )

    submit = SubmitField(label="Submit")
