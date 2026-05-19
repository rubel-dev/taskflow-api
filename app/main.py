from fastapi import FastAPI, Depends
from app.dependencies import get_db
from app.database import SessionLocal

app = FastAPI()
@app.get('/')
def home():
    return{"message":"api is working"}
@app.get('/home')
def getHome(db:SessionLocal= Depends(get_db)):
    return {"hello my dear"}
