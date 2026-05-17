from fastapi import FastAPI

app = FastAPI(
    title = 'TaskFlow API',
    description='A real-world task management backend',
    version = '1.0.0'
)



@app.get('/')
def hello():
    return {"message":"hello world"}

@app.get('/health')
def health_check():
    return {"status":"ok"}