from fastapi import APIRouter, Depends
from auth import AuthManager, User

router = APIRouter()
auth = AuthManager()

@router.post("/register")
def register(user: User):
    return auth.register(user)

@router.post("/login")
def login(user: User):
    return auth.login(user)

@router.get("/protected")
def protected(username: str = Depends(auth.get_current_user)):
    return {"message": "Привет, " + username + "! Ты в защищённой зоне"}