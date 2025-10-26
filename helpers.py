from database import db
from models import User

def check_username_exists(username):
    query = db.session.query(User.id).filter_by(username=username)
    existing_user = query.first()
    if existing_user is not None:
        return True
    else:
        return False