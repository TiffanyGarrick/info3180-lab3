from flask_wtf import FlaskForm
#from wtforms import StringField
from wtforms import Form, BooleanField
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length

#generating secret key for crsf token
WTF_CSRF_SECRET_KEY = '1234' 

class ContactForm(FlaskForm):
    #name = StringField('Name', [validators.Length(min=4, max=25), validators.InputRequired(message='A name is required')])
    #email = StringField('E-mail', [validators.Length(min=6, max=35), validators.Email(message='An email address is required')])
    #subject = StringField('Subject', [validators.InputRequired(message='A subject is required')])
    #messge = StringField('Message', [validators.InputRequired(message='A message is required')])
    name=StringField('Name', validators=[DataRequired(message='A username is required'),Length(min=2, max=25)])
    email = StringField('E-mail', validators=[Length(min=6, max=35), Email(message='An email address is required')])
    subject = StringField('Subject', validators=[DataRequired(message='A subject is required')])
    message = StringField('Message', validators=[DataRequired(message='A message is required')])
    submit=SubmitField('Send')
