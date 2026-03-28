from fastapi import APIRouter
from app.api.v1.endpoints import auth, task

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(task.router, prefix="/tasks", tags=["Tasks"])