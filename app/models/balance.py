from xmlrpc.client import DateTime
from sqlmodel import SQLModel, Field

class Balance(SQLModel, table = True):
    id: int = Field(default=None, primary_key = True)
    user_id: int
    amount: str
    description: str
    current_amount: int
    date: DateTime

    # def get_balance(self, user_id):
    #     return self.__balance.get(user_id)
    #
    # def deposit(self, user_id, amount):
    #     self.__balance.update((user_id, self.get_balance(user_id) + amount))
    #     self.__balance_history.append({'user_id': user_id,
    #                                    'amount': amount,
    #                                    'current_amount': self.get_balance(user_id),
    #                                    'date': datetime.now()})
    #
    # def withdraw(self, user_id, amount):
    #     self.__balance.update((user_id, self.get_balance(user_id) - amount))
    #     self.__balance_history.append({'user_id': user_id,
    #                                    'amount': -amount,
    #                                    'current_amount': self.get_balance(user_id),
    #                                    'date': datetime.now()})
    #
    # def get_history(self):
    #     return self.__balance_history
