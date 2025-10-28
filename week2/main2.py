from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- ユーザーモデル ---
class User(BaseModel):
    username: str
    email: str
    password: str

# --- 仮のDB（リストで代用） ---
users_db = []

# --- ユーザー登録 ---
@app.post("/register")
def register_user(user: User):
    # 同じメールがすでに登録されているかチェック
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    users_db.append(user)
    return {"message": "User registered successfully"}

# --- ユーザー一覧取得 ---
@app.get("/users")
def get_users():
    return users_db

# --- ログイン ---
@app.post("/login")
def login(user: User):
    for u in users_db:
        if u.email == user.email and u.password == user.password:
            return {"message": "Login successful!"}
    raise HTTPException(status_code=401, detail="Invalid credentials")