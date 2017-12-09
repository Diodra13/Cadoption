from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, ValidationError
from wtforms.validators import InputRequired, Email, EqualTo

class RegisterForm(FlaskForm):
	first_name = StringField('First Name:', validators=[InputRequired()])
	last_name = StringField('Last Name:', validators=[InputRequired()])
	email = StringField('Email:', validators=[InputRequired(), Email()])
	password = PasswordField('Password:', validators=[InputRequired(),EqualTo('confirm_password')])
	confirm_password = PasswordField('Confirm Password:')
	phone_number = StringField('Telephone:', [InputRequired()])
	gender = RadioField('Gender:', choices=[('male','Male'),('female','Female'),('other','Other')])
	age_group = RadioField('Age Group:', choices=[('18-25','18-25'),('26-35','26-35'),('36-45','36-45'),('46-55','46-55'),('55+','55+')])
	submit = SubmitField('Submit')

class LoginForm(FlaskForm):
	email = StringField('Email:', validators=[InputRequired(), Email()])
	password = PasswordField('Password:', validators=[InputRequired()])
	submit = SubmitField('Submit')
