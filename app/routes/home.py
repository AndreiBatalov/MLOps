from fastapi import APIRouter

home_route = APIRouter()

@home_route.get('/', tags=['Home'])
async def index() -> str:
    return "Hello World"