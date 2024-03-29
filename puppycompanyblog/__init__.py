# puppycompanyblog/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import flash
from flask_login import LoginManager
import os


app = Flask(__name__)

################################
# Database Setup #
################################
# Set a secret key for form security
app.config['SECRET_KEY'] = 'mysecretkey'

# Configure the SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
Migrate(app, db)


###################################
# Login Configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages

# register blueprint
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

