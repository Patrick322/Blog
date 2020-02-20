from flask import   Flask
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from app.config import config_options

db = SQLAlchemy()
# bcrypt = Bcrypt()
migrate = Migrate()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    # bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)


    from flask import Blueprint
    main = Blueprint('main',__name__)
    from . import views,errors

    return app
