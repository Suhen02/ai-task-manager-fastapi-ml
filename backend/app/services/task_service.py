from app.models.task import Task
from app.ml.predict import predict_category, predict_priority
from app.utils.pagination import paginate

def create_task_service(db, task, user_id):
    text = task.title + " " + task.description

    new_task = Task(
        title=task.title,
        description=task.description,
        category=predict_category(text),
        priority=predict_priority(text),
        user_id=user_id
    )

    db.add(new_task)
    db.commit()
    return new_task


def get_tasks_service(db, user_id, page, limit):
    query = db.query(Task).filter(Task.user_id == user_id)
    return paginate(query, page, limit)