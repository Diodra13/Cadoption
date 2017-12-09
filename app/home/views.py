from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    return render_template('home/index.html', title="Welcome!")

#pws na valw egw kt analogo me dashboard?? 
@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")

    