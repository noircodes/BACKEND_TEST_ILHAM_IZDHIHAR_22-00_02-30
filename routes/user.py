from fastapi import APIRouter, HTTPException, Depends

from models.user import userEntity, usersEntity
from config.db import col
from schemas.user import CreateUser
from bson import ObjectId
from config.jwt import oauth2_scheme, verify_token
from config.hashing import pwd_cxt, Hash

user = APIRouter()

@user.get('/user')
def find_all_users(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    return usersEntity(col.find())

@user.get('/user/{id}')
def find_by_id(id, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    return usersEntity(col.find_one({"_id": ObjectId(id)}))

@user.post('/user')
def create_user(user: CreateUser, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    if col.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    col.insert_one(dict(user))
    return usersEntity(col.find())

@user.put('/user/{id}')
def update_user(id: str, user: CreateUser, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    if col.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    col.find_one_and_update({"_id":ObjectId(id)}, {
        "$set" : dict(user)
    })
    return usersEntity(col.find({"_id":ObjectId}))

@user.delete('/user/{id}')
def delete_user(id, token: str = Depends(oauth2_scheme)):
    verify_token(token)
    return userEntity(col.find_one_and_delete({"_id":ObjectId(id)}))