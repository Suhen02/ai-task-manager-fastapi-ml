from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.user import UserCreate
from app.services.auth_service import register_user, login_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    register_user(db, user)
    return {"success": True}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    token = login_user(db, user)
    return {"success": True, "access_token": token}