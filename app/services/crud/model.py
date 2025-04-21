from models.model import MLModel
from typing import List
from balance import get_balance, withdraw
from event import add_event


def get_all_models(session) -> List[MLModel]:
    return session.query(MLModel).all()

def add_model(filename: str, model_name: str, description: str, session):
    new_model = MLModel(model_name = model_name, filename = filename, description = description)
    session.add(new_model)
    session.commit()
    session.refresh(new_model)

def get_model_by_id(model_id: int, session):
    models = session.get(MLModel, model_id)
    if models:
        return models
    return None

def initialize(model_id: int, session):
    model = session.get(MLModel, model_id)
    """Инициализация модели"""
    pass

def predict(model_id: int, data: str, session):
    """Метод должен запускать модель и возвращать массив:
    [Булевский флаг, предсказание или сообщение об ошибке}"""
    flag = True
    output = ''
    return [flag, output]

def validate_data(data):
    """Метод должен проверять входные данные и возвращать True в случае корректности, иначе False"""
    pass

def request(user_id: int, uploaded_file: str, model_id: int, session):
    if get_balance(user_id = user_id, session = session) >= 100:
        if validate_data(uploaded_file):
            result = predict(model_id = model_id, data = uploaded_file, session = session)
            if result[0]:
                withdraw(user_id = user_id, session = session, amount = 100)
                add_event(user_id = user_id, session = session,
                          amount = 100, action = 'prediction',
                          data = uploaded_file, prediction = result[1])
                return result[1]
            else: return 'Не удалось запустить модель.'
        else: return 'Загруженные данные некорректны.'
    else: return 'Не достаточно средств. Пожалуйста, пополните баланс и попытайтесь снова.'
