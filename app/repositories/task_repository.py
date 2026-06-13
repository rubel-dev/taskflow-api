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

def get_task_by_id_and_user(
    task_id,
    user_id,
    db
):
    task =  db.query(Task).filter(
            Task.id == task_id,
            Task.user_id == user_id,

            ).first()
    return task

def get_task_by_user(
        completed,
        search,
        skip,
        limit,
        db, 
        user_id
):
    query = db.query(Task).filter(Task.user_id == user_id)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    if search is not None:
        query = query.filter(Task.title.ilike(f"%{search}%"))
    query = query.offset(skip).limit(limit)
    return query.all()

def update_task(
        task,
        task_update,
        db
):
    task.title = task_update.title
    task.description = task_update.description
    task.completed=task_update.completed
    db.commit()
    db.refresh(task)
    return task

def delete_task(
        task,
        db
):
    db.delete(task)
    db.commit()
    