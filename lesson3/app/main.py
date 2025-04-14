from models.user import User
import uvicorn
from database.config import get_settings
from database.database import get_session, init_db, engine
from services.crud.user import get_all_users, create_user, set_password
from sqlmodel import Session
from models.history import History
from models.balance import Balance
from services.crud.balance import deposit, withdraw, get_balance
from services.crud.history import get_history, add_event
from models.user import User


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port = 8080, reload = True)
    test_user = User(email='test@mail.ru', name='test1')
    test_user.set_password(test_user.id, 'pass1')

    test_user_2 = User(email='test@mail.ru', name='test2')
    test_user_3 = User(email='test@mail.ru', name='test3')


    init_db()
    print('Init db has been success')

    with Session(engine) as session:
        create_user(test_user, session)
        create_user(test_user_2, session)
        create_user(test_user_3, session)
        users = get_all_users(session)

    for user in users:
        print(f'id: {user.id} - {user.email}')

    test_balance = Balance(test_user.id, amount = 0,
                           description = 'initiallization',current_amount = 0)

    with Session(engine) as session:
        deposit(test_user.id, session, 100)
        get_balance(test_user.id, session)
        withdraw(test_user.id, session, 50)
        get_balance(test_user.id, session)

    with Session(engine) as session:
        add_event(user_id=test_user.id, session=session,
                  amount=50, action='test action',
                  data = 'some data', prediction = 'some prediction'
                )
        get_history(user_id=test_user.id, session=session)


