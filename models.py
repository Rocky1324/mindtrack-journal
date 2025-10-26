from flask_login import UserMixin
from sqlalchemy.orm import DeclarativeBase
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Base(DeclarativeBase):
  pass


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)