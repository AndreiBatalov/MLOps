from datetime import datetime

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
