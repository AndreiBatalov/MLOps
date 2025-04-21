from models.user import User
from services.crud.user import create_user
from models.balance import Balance
from models.event import History
from sqlmodel import SQLModel, Session, create_engine
from .config import get_settings

engine = create_engine(url=get_settings().DATABASE_URL_psycopg,
                       echo=True, pool_size=5, max_overflow=10)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    test_user = User(email='test@mail.ru', name='test1')
    test_user.set_password(test_user.id, 'pass1')
    test_user_2 = User(email='test@mail.ru', name='test2')
    test_user_3 = User(email='test@mail.ru', name='test3')


    with Session(engine) as session:
        create_user(test_user, session)
        create_user(test_user_2, session)
        create_user(test_user_3, session)


    test_balance = Balance(user_id = test_user.id, amount = 0,
                           description = 'initiallization', current_amount = 0)

    test_history = History(user_id = test_user.id, action = 'test history',
                           amount = 0, data = 'test data',
                           prediction = 'test prediction')
