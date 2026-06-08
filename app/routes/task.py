from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

router = APIRouter()

@router.post('/tasks')
def create_task(
    task:TaskCreate,
    db:Session = Depends(get_db)
    
    ):

    new_task = Task(
        title = task.title,
        description = task.description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    

    return new_task

@router.get('/tasks')
def get_tasks(db:Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks



@router.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    db:Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail='task is not found'
        )
    return task

@router.get('/tasks')
def completed_task(
    completed: bool,
    db:Session = Depends(get_db)
):
    tasks = db.query(Task).filter(Task.completed == completed).all()
    return tasks

@router.delete('/tasks/{task_id}')
def delete_task(
    task_id: int,
    db:Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code = 404,
            detail = 'task is not found'
        )
    db.delete(task)
    db.commit()
    return {"message":"Task Deleted"}

@router.put('/tasks/{task_id}')
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db:Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )
    task.title = task_update.title
    task.description = task_update.description
    task.completed = task_update.completed
    db.commit()
    db.refresh(task)
    return task
