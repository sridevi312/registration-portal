import os

class Config:
    SECRET_KEY = b'\xbc\x96\xf8\xdd\xfa\xfef\xf6\xcf\x8a\xf7\xef\xcaH\x1a\xc8q\xf1\xf0<\x03\xe35\xca'  # Use the generated key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
