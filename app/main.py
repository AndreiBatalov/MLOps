from models.user import User
import uvicorn
from database.config import get_settings
from database.database import get_session, init_db, engine
from services.crud.user import get_all_users, create_user, set_password
from sqlmodel import Session
from models.event import History
from models.balance import Balance
from services.crud.balance import deposit, withdraw, get_balance
from services.crud.event import get_history, add_event
from models.user import User


if __name__ == '__main__':
    init_db()
    print('Init db has been success')


