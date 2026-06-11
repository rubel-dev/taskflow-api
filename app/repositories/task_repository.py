from app.models.task import Task
def create_task(
        db,
        title,
        description,
        user_id
):
    task = Task(
        title=title,
        description=description,
        user_id=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task