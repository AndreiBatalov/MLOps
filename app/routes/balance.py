from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.balance import Balance
from services.crud import balance as BalanceService
from typing import List

balance_router = APIRouter(tags=["Balances"])
balances = []

@balance_router.get("/", response_model=List[Balance])
async def retrieve_all_balances() -> List[Balance]:
    return balances

@balance_router.get("/{id}", response_model=Balance)
async def retrieve_balance(id: int) -> Balance:
    for balance in balances:
        if balance.id == id:
            return balance
    raise HTTPException(status_code=status. HTTP_404_NOT_FOUND, detail="Balance with supplied ID does not exist")

@balance_router.post("/new")
async def create_balance(body: Balance = Body(...)) -> dict:
    balances.append(body)
    return {"message": "Balance created successfully"}

@balance_router.delete("/{id}")
async def delete_balance(id: int) -> dict:
    for balance in balances:
        if balance.id == id:
            balances.remove(Balance)
            return {"message": "Balance deleted successfully"}
        raise HTTPException(status_code=status. HTTP_404_NOT_FOUND, detail="Balance with supplied ID does not exist")

@balance_router.delete("/")
async def delete_all_balances() -> dict:
    balances.clear()
    return {"message": "Balances deleted successfully"}

@balance_router.post('/deposit')
async def deposit(user_id: int, amount: int, session = Depends(get_session)) -> dict:
    if BalanceService.get_balance(user_id, session) is None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Balance with such user_id has not been found")
    else:
        BalanceService.deposit(user_id, amount, session)
        return {"message": f"{amount} deposited successfully"}

