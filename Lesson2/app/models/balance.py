from datetime import datetime

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
