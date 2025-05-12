from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate  # Import Flask-Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()  # Initialize Flask-Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Initialize Flask-Migrate with app and db
    migrate.init_app(app, db)

    from app.routes import main
    app.register_blueprint(main)

    return app
