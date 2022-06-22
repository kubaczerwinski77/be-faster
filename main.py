from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from controllers.UserController import User
from routes.UserRouter import router as userRouter
from routes.TextRouter import router as textRouter
from dotenv import load_dotenv

load_dotenv()

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

app.include_router(
  textRouter,
  prefix="/api"
)

initUser = User() 

app.mount("/", StaticFiles(directory="client/build", html=True), name="client")