from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
@home.route('/index')
def index():
    return render_template("home/index.html", title='Welcome!')

@home.route('/find_your_meow')
def find_your_meow():
    return render_template("home/find_your_meow.html", title='find_your_meow')

@home.route('/contact_us')
def contact_us():
    return render_template("home/contact_us.html", title='contact_us')

@home.route('/cat_funnies')
def cat_funnies():
    return render_template("home/cat_funnies.html", title='cat_funnies')

@home.route('/account')
def account():
    return render_template("home/account.html", title='account')

@home.route('/about_us')
def about_us():
    return render_template("home/about_us.html", title='about_us')

    