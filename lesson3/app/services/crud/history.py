from app.models.history import History
from sqlmodel import select
import datetime
from typing import List

def get_history(user_id: int, session) -> List[History]:
    statement = select(History).where(History.user_id == user_id).order_by(History.date.desc())
    return session.exec(statement).all()

def add_event(user_id: int, session, amount: int, action: str, data: str, prediction: str) -> None:
    new_event = History(user_id = user_id,
                          amount = amount,
                          action = action,
                          data = data,
                          date = datetime.now(),
                          prediction = prediction)
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

