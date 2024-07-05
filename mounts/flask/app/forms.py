from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from functions import cmd

# class Lvl_1_Form(FlaskForm):
#     submit = SubmitField('Submit')
#
#     def validate_submit(self):
#         stdout, stderr = cmd("check1.sh")
#         if stdout == 'incorrect':
#             raise ValidationError("The file does not exist!")