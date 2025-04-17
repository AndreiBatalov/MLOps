from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.model import MLModel
from services.crud import model as ModelService


model_router = APIRouter(tags=["MLModels"])

@model_router.post('/deposit')
async def request(user_id: int, uploaded_file: str, model_id: int, session = Depends(get_session)) -> dict:
   return {"message": f'{ModelService.request(user_id, uploaded_file, model_id, session)}'}
