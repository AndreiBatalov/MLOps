from xmlrpc.client import DateTime
from sqlmodel import SQLModel, Field

class Event(SQLModel, table = True):
    id: int = Field(default=None, primary_key = True)
    user_id: int
    action: str
    amount: int
    data: str
    prediction: str
    date: DateTime

# class History:
#     def __init__(self):
#         self.history = []
#
#     def add_event(self, user_id, action, amount, data, prediction):
#         entry = {'user_id': user_id,
#                  'action': action,
#                  'amount': amount,
#                  'data':data,
#                  'prediction': prediction,
#                  'date': datetime.now()
#                  }
#         self.history.append(entry)
#
#     def get_history(self):
#         return self.history
