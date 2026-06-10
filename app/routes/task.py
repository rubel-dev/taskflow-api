from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()

@router.post('/tasks', response_model=TaskResponse, status_code=201)
def create_task(
    task:TaskCreate,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
    
    ):

    new_task = Task(
        title = task.title,
        description = task.description,
        user_id = user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    

    return new_task

@router.get('/tasks', response_model=list[TaskResponse], status_code=200)
def get_tasks(
    completed: bool | None = None,
    search: str | None = None,
    skip:int = 0,
    limit:int = 10,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    query = db.query(Task).filter(Task.user_id == user_id)
    if completed is not None:
        query.filter(Task.completed == completed)
    if search is not None:
        query.filter(Task.title.ilike(f"%{search}%"))
    query.offset(skip).limit(limit)
    return query.all()



@router.get("/tasks/{task_id}", response_model = TaskResponse, status_code=200)
def get_task(
    task_id: int,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
        ).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail='task is not found'
        )
    return task



@router.delete('/tasks/{task_id}', status_code=204)
def delete_task(
    task_id: int,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
        ).first()
    if not task:
        raise HTTPException(
            status_code = 404,
            detail = 'task is not found'
        )
    db.delete(task)
    db.commit()
    return {"message":"Task Deleted"}

@router.put('/tasks/{task_id}', response_model= TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
        ).first()
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
