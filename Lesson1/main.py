from datetime import datetime
import hashlib
import os

class Balance:
    def __init__(self):
        self.__balance = {}
        self.__balance_history = []

    def get_balance(self, user_id):
        return self.__balance.get(user_id)

    def deposit(self, user_id, amount):
        self.__balance.update((user_id, self.get_balance(user_id) + amount))
        self.__balance_history.append({'user_id': user_id,
                                       'amount': amount,
                                       'current_amount': self.get_balance(user_id),
                                       'date': datetime.now()})

    def withdraw(self, user_id, amount):
        self.__balance.update((user_id, self.get_balance(user_id) - amount))
        self.__balance_history.append({'user_id': user_id,
                                       'amount': -amount,
                                       'current_amount': self.get_balance(user_id),
                                       'date': datetime.now()})

    def get_history(self):
        return self.__balance_history

Balance = Balance()

class History:
    def __init__(self):
        self.history = []

    def add_transaction(self, user_id, action, amount, data, prediction):
        entry = {'user_id': user_id,
                 'action': action,
                 'amount': amount,
                 'data':data,
                 'prediction': prediction,
                 'date': datetime.now()
                 }
        self.history.append(entry)

    def get_history(self):
        return self.history

History = History()

class MLModel:
    def __init__(self, filename):
        self.filename = filename
        self.output = ''

    def upload (self, filename):
        """Загрузка модели"""
        pass

    def initialize(self):
        """Инициализация модели"""
        pass

    def predict(self, data):
        """Метод должен запускать модель и возвращать массив:
        [Булевский флаг, предсказание или сообщение об ошибке}"""
        flag = True
        return [flag, self.output]


LinReg = MLModel('some_file')

class MLTask:
    def __init__(self, data):
        self.data = data

    def validate_data(self, data):
        """Метод должен проверять входные данные и возвращать True в случае корректности, иначе False"""
        pass

    def request(self, uploaded_file, user_id):
        if Balance.get_balance(user_id) >= 100:
            if self.validate_data(uploaded_file):
                result = LinReg.predict(uploaded_file)
                if result[0]:
                    History.add_transaction(user_id, 'prediction', -100, uploaded_file, result[1])
                    Balance.withdraw(user_id, 100)
                    return result[1]
                else: return 'Не удалось запустить модель.'
            else: return 'Загруженные данные некоректны.'
        else: return 'Не достаточно средств. Пожалуйста, пополните баланс и попытайтесь снова.'

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








