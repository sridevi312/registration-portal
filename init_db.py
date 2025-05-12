# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'  # or your DB URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)    # <– this wires up Flask-Migrate to your app:contentReference[oaicite:1]{index=1}

from . import models  # ensure models are imported so Alembic sees them:contentReference[oaicite:2]{index=2}
