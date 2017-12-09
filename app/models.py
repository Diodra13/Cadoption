from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):

    __tablename__ = 'users'   

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    gender = db.Column(db.String(10))
    birthdate = db.Column(db.Date)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    cat_image = db.Column(BLOB)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship('User', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post: {}>'.format(self.name)

class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Tag: {}>'.format(self.name)

class Tagged_post(db.Model):

    __tablename__ = 'tagged_posts'

    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.relationship('Tag', backref='tagged_post', lazy='dynamic')
    post_id = db.relationship('Post', backref='tagged_post', lazy='dynamic')

    def __repr__(self):
        return '<Tagged_post: {}>'.format(self.name)
        