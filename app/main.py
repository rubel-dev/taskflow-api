from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.dependencies import get_db

app = FastAPI(
    title = 'TaskFlow API',
    description='A real-world task management backend',
    version = '1.0.0'
)



@app.get('/')
def root(db:Session = Depends(get_db)):
    return {"message":"working well"}
@app.get('/health')
def health_check():
    return {"status":"ok"}