from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = []


def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# --- ユーザー登録 ---
@app.post("/register")
def register_user(user: User):
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user.password)
    user.password = hashed_pw
    users_db.append(user)
    return {"message": "User registered successfully"}

# --- ユーザー一覧取得---
@app.get("/users")
def get_users():
    return users_db

# --- ログイン ---
@app.post("/login")
def login(user: User):
    for u in users_db:
        if u.email == user.email:
            if verify_password(user.password, u.password):
                return {"message": "Login successful!"}
            else:
                raise HTTPException(status_code=401, detail="Incorrect password")
    raise HTTPException(status_code=404, detail="User not found")
