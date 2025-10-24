from flask_login import UserMixin
from sqlalchemy.orm import DeclarativeBase
from app import db


class Base(DeclarativeBase):
  pass

class User(UserMixin, db.Model):
    id = db.Column()
