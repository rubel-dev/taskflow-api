from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.database import engine, Base
from app.models.task import Task
from app.routes.task import router as task_router

Base.metadata.create_all(bind = engine)
app = FastAPI()
app.include_router(task_router)

@app.get('/')
def home(db:Session = Depends(get_db)):
    return {"message":"working"}

