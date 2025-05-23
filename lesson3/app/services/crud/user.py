from app.models.user import User
from typing import List, Optional
import os
import hashlib

def set_password(user_id: int, password: str, session) -> None:
    user = session.query(User).filter_by(id=user_id).first()
    salt = os.urandom(32)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    user.password = hashed_password + b';' + salt
    session.commit()

def get_all_users(session) -> List[User]:
    return session.query(User).all()

def get_user_by_id(id:int, session) -> Optional[User]:
    users = session.get(User, id)
    if users:
        return users
    return None

def get_user_by_email(email:str, session) -> Optional[User]:
    user = session.query(User).filter(User.email == email).first()
    if user:
        return user
    return None

def create_user(new_user: User, session) -> None:
    session.add(new_user)
    session.commit()
    session.refresh(new_user)


