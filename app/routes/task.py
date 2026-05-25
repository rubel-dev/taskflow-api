from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from fastapi import HTTPException

router = APIRouter()

@router.post('/tasks')
def createTask(
    task: TaskCreate,
    db: Session = Depends(get_db)
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
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return tasks

@router.get('/tasks/{task_id}')
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail='task not found'
        )
    return task

@router.delete('/tasks/{task_id}')
def delete_task(
    task_id: int,
    db:Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail='Task not found'
        )
    db.delete(task)
    db.commit()
    return {"message":"Task deleted"}


@router.put('/tasks/{task_id}')
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail = 'Task not found'

        )
    task.title = update_task.title
    task.description = update_task.description
    task.completed = update_task.completed
    db.commit()
    db.refresh(task)
    return task

