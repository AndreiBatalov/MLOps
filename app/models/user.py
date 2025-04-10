import hashlib
import os
from app.models.balance import Balance
from app.models.history import History

class User:
    def __init__(self, user_id, nickname, name, surname, birth_date, gender):
        self.user_id = user_id
        self.nickname = nickname
        self.__password = None
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender

    def set_password(self, password):
        salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        self.__password = hashed_password + ';' + salt

    def get_data(self):
        return {'user_id': self.user_id,
        'nickname': self.nickname,
        'password': self.__password,
        'name' : self.name,
        'surname' : self.surname,
        'birth date' : self.birth_date,
        'gender' : self.gender}

class Admin(User):
    @staticmethod
    def change_balance(user_id, amount):
        if amount > 0: Balance.deposit(user_id, amount)
        else: Balance.withdraw(user_id, amount)

    @staticmethod
    def see_balance_history():
        return Balance.get_history()

    @staticmethod
    def see_transaction_history():
        return History.get_history()

    @staticmethod
    def see_user_balance(user_id):
        return Balance.get_balance(user_id)