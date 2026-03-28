
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.error_handler import app_exception_handler, generic_exception_handler
from app.core.exceptions import AppException
from app.db.database import Base, engine
from app.middleware.request_logger import RequestLoggerMiddleware
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Task Manager V2")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(RequestLoggerMiddleware)


app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


app.include_router(api_router, prefix="/api/v1")