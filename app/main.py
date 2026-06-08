from fastapi import Depends, FastAPI

from sqlalchemy.orm import Session

from app.database import Base, engine
from app.dependencies import get_db
from app.schemas.task import TaskCreate
from app.routes.task import router as task_router

app = FastAPI()
app.include_router(task_router)
Base.metadata.create_all(bind = engine)
@app.get('/')
def root():
    return {"message":"python backend is working"}

@app.get('/home')
def home(db:Session = Depends(get_db)):
    return {"message":"yes, i am working properly"}

 