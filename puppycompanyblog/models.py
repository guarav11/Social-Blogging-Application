# Import necessary modules and components
from puppycompanyblog import db, login_manager  # Importing the database instance and login manager
from werkzeug.security import generate_password_hash, check_password_hash  # Importing password hashing functions
from flask_login import UserMixin  # Importing UserMixin for user authentication
from datetime import datetime  # Importing datetime module for timestamping

# Define a function to load a user by ID for the login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Define the User model class
class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Table name for the User model

    # Define columns for the User table
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # Define relationship with BlogPost model
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    # Constructor to initialize User object
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    # Method to check password validity
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Representation of User object
    def __repr__(self):
        return f"Username {self.username}"

# Define the BlogPost model class
class BlogPost(db.Model):
    __tablename__ = 'blog_post'  # Table name for the BlogPost model

    # Define columns for the BlogPost table
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)

    # Define relationship with User model
    users = db.relationship(User)

    # Constructor to initialize BlogPost object
    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    # Representation of BlogPost object
    def __repr__(self):
        return f"Post ID: {self.id}  --  Date: {self.date} -- Title: {self.title}"
