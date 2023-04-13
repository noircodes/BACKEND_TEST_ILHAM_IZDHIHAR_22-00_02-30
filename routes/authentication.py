from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta


from schemas.login import Login
from models.user import userEntity
from config.db import col
from config.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from config.jwt import oauth2_scheme, verify_token

login = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authenticate_user(username: str, password: str):
    user = col.find_one({"username": username})
    if user and user["password"] == password:
        return user

@login.post("/login")
def log_in(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    status = str(user['status']).upper()
    if status == "FALSE":
        raise HTTPException(status_code=400, detail="Status tidak aktif")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user["_id"])}, expires_delta=access_token_expires
    )
    return {"status_code": 200, "message": "Berhasil Login", "access_token": access_token, "data": {
        "id" : str(user['_id']),
        "name" : user['name'],
        "email" : user['email'],
        "phone" : user['phone'],
        "exp" : access_token_expires
    }}

# Membuat route untuk melindungi rute dengan otentikasi
@login.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    return 'protected'