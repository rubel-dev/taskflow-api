from app.models.task import Task
from app.repositories import task_repository
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