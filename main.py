from fastapi import FastAPI
from routes.user import user
from routes.authentication import login

app = FastAPI()

app.include_router(user)
app.include_router(login)
