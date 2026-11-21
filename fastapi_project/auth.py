import os
import jwt
import datetime
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

SECRET = os.getenv("SECRET_KEY", "super_secret_key")
security = HTTPBearer()

class User(BaseModel):
    username: str
    password: str

class AuthManager:
    def __init__(self):
        self.users = {} # В реальном проекте тут была бы база данных

    def register(self, user: User):
        if user.username in self.users:
            raise HTTPException(status_code=400, detail="Пользователь уже есть")
        self.users[user.username] = user.password
        return {"message": "Зарегистрирован"}

    def login(self, user: User):
        if self.users.get(user.username) != user.password:
            raise HTTPException(status_code=401, detail="Неверный логин или пароль")
        return {"token": self.create_token(user.username)}

    def create_token(self, username: str):
        payload = {
            "sub": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET, algorithm="HS256")

    def get_current_user(self, credentials: HTTPAuthorizationCredentials = Depends(security)):
        try:
            token = credentials.credentials
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Токен истёк")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Неверный токен")