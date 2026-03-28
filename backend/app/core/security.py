from passlib.context import CryptContext
from jose import jwt
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    password = password[:72]  
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str):
    password = password[:72]  
    return pwd_context.verify(password, hashed)


def create_token(data: dict):
    return jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")