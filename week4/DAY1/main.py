from fastapi import FastAPI
from . import models
from .database import engine

app = FastAPI()

# テーブルを作成
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "DB連携タスク管理APIへようこそ！"}
