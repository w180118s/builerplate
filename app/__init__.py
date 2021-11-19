from flask import Flask, session
from flask_session import Session
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import request

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rahasia@127.0.0.1/db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Pasien

    @login_manager.user_loader
    def load_user(user_id):
        login_type = session.get('level')
        print('===========')
        print(login_type)
        print('===========')
        if login_type == 'admin':
            return User.query.get(int(user_id))
        else:
            return Pasien.query.get(int(user_id))
            
        # since the user_id is just the primary key of our user table, use it in the query for the user
        # return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
 
