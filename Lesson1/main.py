class Model:
    def __init__(self, filename, input):
        self.filename = filename
        self.input = input
        self.output = ''

    def validate_input(self, input):
        """Метод должен проверять входные данные и возвращать True в случае корректности, иначе False"""
        pass

    def run_model(self, filename, input):
        """Метод должен запускать модель и возвращать True в случае успешной работы, иначе False"""
        pass

    def get_data(self):
        """Получение последнего ввода и вывода вывода"""
        pass

from datetime import datetime

class History:
    def __init__(self):
        self.history = []

    def add_transaction(self, user_id, action, amount):
        entry = {'user_id': user_id,
                 'action': action,
                 'amount': amount,
                 'input': Model.get_data()[0],
                 'output': Model.get_data()[1],
                 'date': datetime.now()
                 }
        self.history.append(entry)

class User:
    def __init__(self, id, is_admin, name, surname, birth_date, gender, balance):
        self.id = id
        self.is_admin = is_admin
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.__balance = balance
        self.__history = History()

    def request_model(self, uploaded_file):
        if self.__balance >= 100:
            if Model.validate_input(uploaded_file):
                if Model.run_model(uploaded_file):
                    self.__history.add_transaction(self.id, 'Списание за услугу', '-100')
                    self.__balance -= 100
                    return Model.get_data()[1]
                else: return 'Не удалось запустить модель.'
            else: return 'Загруженные данные некоректны.'
        else: return 'Не достаточно средств. Пожалуйста, пополните баланс и попытайтесь снова.'

    def get_balance(self):
        return self.__balance

    def make_deposit(self, amount):
        self.__balance += amount

    def get_history(self):
        return self.__history.history