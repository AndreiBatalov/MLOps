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

from balance import Balance
from history import History

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
                    History.add_event(user_id, 'prediction', -100, uploaded_file, result[1])
                    Balance.withdraw(user_id, 100)
                    return result[1]
                else: return 'Не удалось запустить модель.'
            else: return 'Загруженные данные некоректны.'
        else: return 'Не достаточно средств. Пожалуйста, пополните баланс и попытайтесь снова.'