from app.models.balance import Balance
from sqlmodel import select
import datetime
from typing import List

def get_balance(user_id: int, session) -> int:
    statement = select(Balance).where(Balance.user_id == user_id).order_by(Balance.date.desc())
    balance = session.exec(statement).first()
    return balance.current_amount()

def deposit(user_id: int, session, amount: int) -> None:
    new_balance = Balance(user_id = user_id,
                          amount = amount,
                          description = f'deposit +{amount}',
                          current_amount = get_balance(user_id, session)+amount,
                          date = datetime.now())
    session.add(new_balance)
    session.commit()
    session.refresh(new_balance)

def withdraw(user_id: int, session, amount: int) -> None:
    new_balance = Balance(user_id = user_id,
                          amount = amount,
                          description = f'deposit -{amount}',
                          current_amount = get_balance(user_id, session)-amount,
                          date = datetime.now())
    session.add(new_balance)
    session.commit()
    session.refresh(new_balance)

def get_history(user_id: int, session) -> List[Balance]:
    return session.query(Balance).filter_by(user_id = user_id).all()

# def deposit(self, user_id, amount):
#     self.__balance.update((user_id, self.get_balance(user_id) + amount))
#     self.__balance_history.append({'user_id': user_id,
#                                    'amount': amount,
#                                    'current_amount': self.get_balance(user_id),
#                                    'date': datetime.now()})
#  id: int = Field(default=None, primary_key = True)
# def withdraw(self, user_id, amount):
#     self.__balance.update((user_id, self.get_balance(user_id) - amount))
#     self.__balance_history.append({'user_id': user_id,
#                                    'amount': -amount,
#                                    'current_amount': self.get_balance(user_id),
#                                    'date': datetime.now()})
#
# def get_history(self):
#     return self.__balance_history