from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from models.model import User

app = FastAPI()

from database import (
  fetch_one_user,
  fetch_all_users,
  create_user,
  remove_user
)

origins = ["https://localhost:3000"]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/api") 
def hello():
  return { "message": "Hello, world!!" }

@app.get("/api/user")
async def get_users():
  response = await fetch_all_users()
  return response

@app.get("/api/user{id}", response_model=User)
async def get_user_by_id(id):
  response = await fetch_one_user(id)
  if response:
    return response
  raise HTTPException(404, f"There is no user with id {id}")

@app.post("/api/user", response_model=User)
async def post_user(user: User):
  response = await create_user(user.dict())
  if response:
    return response
  raise HTTPException(400, "Something went wrong / Bad request")

@app.delete("/api/user{id}")
async def delete_user(id):
  response = await remove_user(id)
  if response:
    return f"Succesfully deleted user with id {id}"
  raise HTTPException(400, f"There is no user with id {id}")
  



app.mount("/", StaticFiles(directory="client/build", html=True), name="client")