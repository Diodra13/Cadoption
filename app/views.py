from flask import render_template
from app import app
from .forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')

@app.route('/find_your_meow')
def find_your_meow():
    return render_template("find_your_meow.html",
                           title='find_your_meow')

@app.route('/rescued_meows')
def rescued_meows():
    return render_template("rescued_meows.html",
                           title='rescued_meows')

@app.route('/about_meows')
def about_meows():
    return render_template("about_meows.html",
                           title='about meows')

@app.route('/about_us')
def about_us():
    return render_template("about_us.html",
                           title='about us')

@app.route('/admin_page')
def admin_page():
    return render_template("admin_page.html",
                           title='admin_page')

@app.route('/sign_up', methods=['post','get'])
def sign_up():
  form = RegisterForm()

  return render_template("sign_up.html",
                           title='sign_up',
                           form=form)

@app.route('/login', methods=['post','get'])
def login():
  form = LoginForm()

  return render_template("login.html",
                           title='login',
                           form=form)