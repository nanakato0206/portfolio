import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# このファイル(database.py)自身があるフォルダを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 絶対パスでDBファイルを指定（どこで実行しても week4/task.db に作られる）
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'task.db')}"
# データベースと接続するためのエンジンを作成（既存名：create_engine）
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# データベース操作のためのSessionLocalを作成（既存名：sessionmaker）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルクラスの基底クラスを作成（既存名：declarative_base）
Base = declarative_base()