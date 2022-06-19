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

@app.post("/token")
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    userDict = await initUser.fetch_one_user_by_username(formData.username)
    if not userDict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserCreate(**userDict)
    if not verifyPassword(formData.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

app.mount("/", StaticFiles(directory="client/build", html=True), name="client")