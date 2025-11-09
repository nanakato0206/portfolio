
from sqlalchemy.orm import Session
from . import models

#  全タスクを取得
def get_all_tasks(db: Session):
    return db.query(models.Task).all()

#  タスクを新規作成
def create_task(db: Session, title: str, deadline: float, description: str = None):
    task = models.Task(title=title, deadline=deadline, description=description)
    db.add(task)        
    db.commit()         
    db.refresh(task)    
    return task

#  タスクを更新
def update_task(db: Session, task_id: int, title: str, deadline: float):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.title = title
        task.deadline = deadline
        db.commit()
        db.refresh(task)
        return task
    return None

# タスクを削除
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
