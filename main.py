from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from routes.UserRouter import router as userRouter

app = FastAPI()

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="token")

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

@app.get("/api/items") 
async def read_items(token: str = Depends(oauth2Scheme)):
  return { "token": token }

app.mount("/", StaticFiles(directory="client/build", html=True), name="client")