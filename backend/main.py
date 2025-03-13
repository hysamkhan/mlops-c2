from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/signup")
def signup(user: User):
    return {"message": f"User {user.username} signed up successfully!"}

@app.post("/login")
def login(user: User):
    return {"message": f"User {user.username} logged in!"}