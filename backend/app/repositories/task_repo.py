def get_tasks_by_user(db, user_id):
    return db.query(Task).filter(Task.user_id == user_id)