from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services import task_service

router = APIRouter()

@router.post('/tasks', response_model=TaskResponse, status_code=201)
def create_task(
    task:TaskCreate,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
    
    ):
 
    return task_service.create_task(
        task=task,
        user_id=user_id,
        db=db
    )

@router.get('/tasks', response_model=list[TaskResponse], status_code=200)
def get_tasks(
    completed: bool | None = None,
    search: str | None = None,
    skip:int = 0,
    limit:int = 10,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    return task_service.get_tasks(
        completed=completed,
        search=search,
        skip=skip,
        limit=limit,
        db=db,
        user_id=user_id
    )
    



@router.get("/tasks/{task_id}", response_model = TaskResponse, status_code=200)
def get_task(
    task_id: int,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    return task_service.get_task(
        task_id = task_id,
        user_id = user_id,
        db = db
    )


   



@router.delete('/tasks/{task_id}', status_code=204)
def delete_task(
    task_id: int,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    return task_service.delete_task(
        task_id=task_id,
        user_id=user_id,
        db=db
    )
    


@router.put('/tasks/{task_id}', response_model= TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db:Session = Depends(get_db),
    user_id:int = Depends(get_current_user)
):
    return task_service.update_task(
        task_id=task_id,
        task_update=task_update,
        user_id=user_id,
        db=db
    )
