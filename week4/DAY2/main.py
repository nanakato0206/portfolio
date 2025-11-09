from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud
from .database import engine, SessionLocal
from datetime import date


# FastAPIアプリ作成
app = FastAPI()

# テーブル作成（Day1で作った部分）
models.Base.metadata.create_all(bind=engine)

#  DBセッションを取得する依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  ルート
@app.get("/")
def read_root():
    return {"message": "これはタスク管理を行うAPIです！"}

#  全件取得
@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db)

#  新規作成
@app.post("/tasks/")
def create_task(title: str, deadline: date = None, description: str = None, db: Session = Depends(get_db)):
    return crud.create_task(db, title, deadline, description)

#  更新
@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, deadline: date, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, title, deadline)
    if not task:
        raise HTTPException(status_code=404, detail="タスクが見つかりませんでしたmm")
    return task

#  削除
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="タスクが見つかりませんでしたmm")
    return {"message": f"タスク {task_id} の削除に成功しました！( ^)o(^ )"}
