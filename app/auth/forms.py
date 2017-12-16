from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, RadioField, ValidationError
from wtforms.validators import InputRequired, Email, EqualTo

from .. models import User


class RegisterForm(FlaskForm):
	first_name = StringField('First Name:', validators=[InputRequired()])
	last_name = StringField('Last Name:', validators=[InputRequired()])
	email = StringField('Email:', validators=[InputRequired(), Email()])
	password = PasswordField('Password:', validators=[InputRequired(),EqualTo('confirm_password')])
	confirm_password = PasswordField('Confirm Password:')
	phone_number = StringField('Telephone:', [InputRequired()])
	birth_date = DateField('Date of Birth:', format='%m/%d/%Y')
	gender = RadioField('Gender:', choices=[('male','Male'),('female','Female'),('other','Other')])
	submit = SubmitField('Submit')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email is already in use.')

class LoginForm(FlaskForm):
	email = StringField('Email:', validators=[InputRequired(), Email()])
	password = PasswordField('Password:', validators=[InputRequired()])
	submit = SubmitField('Submit')

