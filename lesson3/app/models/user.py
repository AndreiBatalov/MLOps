import hashlib
import os
from app.models.balance import Balance
from app.models.history import History
from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional, List

class User(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    email: str
    password: None
    nickname: str
    name: str
    surname: str
    birth_date: str
    gender: str
    events: Optional[str]

    # def set_password(self, password):
    #     salt = os.urandom(32)
    #     hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    #     self.__password = hashed_password + b';' + salt
    #
    # def get_data(self):
    #     return {'user_id': self.user_id,
    #     'nickname': self.nickname,
    #     'password': self.__password,
    #     'name' : self.name,
    #     'surname' : self.surname,
    #     'birth_date' : self.birth_date,
    #     'gender' : self.gender}

