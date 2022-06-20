from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from controllers.UserController import User, UserCreate
from routes.UserRouter import router as userRouter
from utils import oauth2Scheme, verifyPassword

app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(
  userRouter,
  prefix="/api"
)

initUser = User() 

app.mount("/", StaticFiles(directory="client/build", html=True), name="client")