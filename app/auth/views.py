from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import RegisterForm, LoginForm
from .. import db
from ..models import User

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
	register_form = RegisterForm()
	if register_form.validate_on_submit():
		user = User(first_name=register_form.first_name.data,
					last_name=register_form.last_name.data,        			
					email=register_form.email.data,
					password=register_form.password.data,
					gender=register_form.gender.data,
					phone_number=register_form.phone_number.data,
					birth_date=register_form.birth_date.data
					)

		db.session.add(user)
		db.session.commit()
		flash('You have successfully registered! You may now login.')

		return redirect(url_for('auth.login'))

	return render_template("auth/sign_up.html", title='sign_up', register_form=register_form)

@auth.route('/login', methods=['GET', 'POST'])
def login():

	login_form = LoginForm()
	if login_form.validate_on_submit():
		user = User.query.filter_by(email=login_form.email.data).first()
		if user is not None and user.verify_password(login_form.password.data):
			login_user(user)
			return redirect(url_for('home.index'))
	else:
		flash('Invalid email or password.')

	return render_template("auth/login.html", title='login', login_form=login_form)

@auth.route('/logout')
@login_required
def logout():

	logout_user()
	flash('You have successfully been logged out.')

	return redirect(url_for('auth.login'))


