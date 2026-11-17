from fastapi import APIRouter, Depends
from auth import User, AuthManager
from dependencies import get_auth_manager

router = APIRouter()

@router.post("/register")
def register(user: User, auth: AuthManager = Depends(get_auth_manager)):
    return auth.register(user)

@router.post("/login")
def login(user: User, auth: AuthManager = Depends(get_auth_manager)):
    return auth.login(user)

@router.get("/protected")
def protected(username: str = Depends(get_auth_manager().get_current_user)):
    return {"message": "Привет, " + username + "! Ты в защищённой зоне"}