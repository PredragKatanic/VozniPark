from fastapi import APIRouter

from .vozilo import router as vozila_router

api_router = APIRouter()
api_router.include_router(vozila_router, prefix="/vozila", tags=["Vozila"])

