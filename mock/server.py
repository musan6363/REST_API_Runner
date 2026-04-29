from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI(title="mock server")

class StatusUpdate(BaseModel):
    message: str

# Dummy User Template
class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Server is running!"}

@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict[str, Any]:
    """指定されたIDのユーザー情報を返す"""
    return {
        "id": user_id,
        "name": "研修 太郎",
        "email": "taro@example.com",
        "role": "Admin"
    }

@app.post("/add_user", status_code=200)
async def create_user(user: User) -> dict[str, Any]:
    # dummy
    # register user process...
    return {"message": "Successfully registered", "user": user}

@app.post("/status", status_code=300)
async def post_status(update: StatusUpdate) -> dict[str, Any]:
    """ステータスメッセージを受け取って成功を返す"""
    return {
        "status": "success",
        "received_message": update.message
    }
