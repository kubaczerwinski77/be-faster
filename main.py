from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes.UserRouter import router as userRouter

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

@app.get("/api") 
def hello():
  return { "message": "Hello, world!!" }

app.mount("/", StaticFiles(directory="client/build", html=True), name="client")