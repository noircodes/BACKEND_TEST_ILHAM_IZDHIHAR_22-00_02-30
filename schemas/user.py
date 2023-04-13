from pydantic import BaseModel
import datetime

class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    username: str
    password: str
    status : bool
    createdTime: datetime.datetime
    createdBy: str
    updatedTime: datetime.datetime
    updatedBy: str
    
class CreateUser(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    username: str
    password: str
    status : bool
    createdTime: datetime.datetime
    createdBy: str
    updatedTime: datetime.datetime
    updatedBy: str