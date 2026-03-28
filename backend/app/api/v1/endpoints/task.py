from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task_service, get_tasks_service
from app.middleware.auth_middleware import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_task(task: TaskCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    result = create_task_service(db, task, user["id"])

    return {
        "success": True,
        "data": TaskResponse.model_validate(result)  # 🔥 FIX
    }


@router.get("/")
def get_tasks(page: int = 1, limit: int = 10, user=Depends(get_current_user), db: Session = Depends(get_db)):
    tasks = get_tasks_service(db, user["id"], page, limit)

    return {
        "success": True,
        "data": [TaskResponse.model_validate(task) for task in tasks]  # 🔥 FIX
    }