from fastapi import APIRouter, FastAPI
from services.userServices import userLogin
from services.userServices import registerUser
from interface.user import User
from interface.login import Login

router =  APIRouter()


@router.post('/register')
async def register(user:User):
    print(user.name)
    return registerUser(user)

@router.post('/login')
async def login(login:Login):
    return userLogin(login)

    