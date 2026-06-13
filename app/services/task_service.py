from app.models.task import Task
from app.repositories import task_repository
from fastapi import HTTPException

def create_task(
        task,
        user_id,
        db
):
    return task_repository.create_task(
        db=db,
        title=task.title,
        description=task.description,
        user_id=user_id
    )

def get_task(
    task_id,
    user_id,
    db
):
    task = task_repository.get_task_by_id_and_user(
        task_id = task_id,
        user_id=user_id,
        db=db
    )
    if not task:
        raise HTTPException(
            status_code = 404,
            detail = 'Task Not Found'
        )
    return task

def get_tasks(
        completed,
        search,
        skip,
        limit,
        user_id,
        db

):
    return task_repository.get_task_by_user(
        completed=completed,
        search=search,
        skip=skip,
        limit=limit,
        user_id=user_id,
        db=db
    )
    

def update_task(
        task_id,
        task_update,
        user_id,
        db
):
    task = task_repository.get_task_by_id_and_user(
        task_id=task_id,
        user_id=user_id,
        db=db
    )
    if not task:
        raise HTTPException(
            status_code=404,
            detail='Task Not Found'
        )
    return task_repository.update_task(
        task = task,
        task_update =  task_update,
        db = db
    )

def delete_task(
        task_id,
        user_id,
        db
):
    task = task_repository.get_task_by_id_and_user(
        task_id=task_id,
        user_id=user_id,
        db=db
    )
    if not task:
        raise HTTPException(
            status_code=404,
            detail='Task Not Found'
        )
    task_repository.delete_task(
        task = task,
        db=db
    )
    return None