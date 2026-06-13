from fastapi import Depends, FastAPI

from sqlalchemy.orm import Session

from app.database import Base, engine
from app.dependencies import get_db
from app.schemas.task import TaskCreate
from app.routes.task import router as task_router
from app.routes.user import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from app.exceptions.custom_exceptions import AppException
from app.exceptions.handlers import app_exception_handler


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://127.0.0.1:5500'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)
app.add_exception_handler(
    AppException,
    app_exception_handler
)
app.include_router(task_router)
app.include_router(user_router)
 
@app.get('/')
def root():
    return {"message":"python backend is working"}
 