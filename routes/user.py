from fastapi import APIRouter
from models.user import User
from config.db import conn

user = APIRouter()

@user.get("/")
async def findAllUsers():
  return conn.local.user.find()