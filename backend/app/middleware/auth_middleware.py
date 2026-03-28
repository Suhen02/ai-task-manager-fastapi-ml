from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from app.core.config import settings

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        return jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")