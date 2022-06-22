from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from controllers.TokenController import createAccessToken
from models.UserModels import UserCreate, UserBase
from controllers.UserController import User
from jose import jwt, JWTError
from utils import oauth2Scheme
from models.TokenModels import TokenData, Token
from datetime import timedelta
import os

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

initUser = User()

@router.get("/", tags=["users"])
async def get_users():
  response = await initUser.fetch_all_users()
  return response

@router.get("/stats/{id}", tags=["users"])
async def get_stats_by_user_id(id):
  response = await initUser.fetch_stats_by_user_id(id)
  return response

@router.post("/", response_model=UserCreate)
async def post_user(user: UserBase):
  # check if user with this email exists
  emailExists = await initUser.fetch_one_user_by_email(user.email)
  if (emailExists):
    raise HTTPException(409, "User with this email already exists")

  # check if user with this email exists
  usernameExists = await initUser.fetch_one_user_by_username(user.username)
  if (usernameExists):
    raise HTTPException(409, "User with this username already exists")

  # create user
  response = await initUser.create_user(user.dict())

  if response:
    return response
  raise HTTPException(400, "Something went wrong / Bad request")

@router.delete("/{id}")
async def delete_user(id):
  response = await initUser.remove_user(id)
  if response:
    return f"Succesfully deleted user with id {id}"
  raise HTTPException(400, f"There is no user with id {id}")

# authentication zone
async def getCurrentUser(token: str = Depends(oauth2Scheme)):
    credencialsException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("sub")
        if username is None:
            raise credencialsException
        token_data = TokenData(username=username)
    except JWTError:
        raise credencialsException
    user = await initUser.fetch_one_user_by_username(username=token_data.username)
    if user is None:
        raise credencialsException
    user = UserBase(**user)
    return user


async def getCurrentActiveUser(currentUser: UserBase = Depends(getCurrentUser)):
    if currentUser.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return currentUser

@router.get("/me")
async def read_users_me(currentUser: UserCreate = Depends(getCurrentActiveUser)):
  return currentUser

@router.get("/{id}", response_model=UserCreate)
async def get_user_by_id(id):
  response = await initUser.fetch_one_user_by_id(id)
  if response:
    return response
  raise HTTPException(404, f"There is no user with id {id}")

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await initUser.authenticateUser(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    accessTokenExpires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    accessToken = createAccessToken(
        data={"sub": user.username}, expiresDelta=accessTokenExpires
    )
    return {"access_token": accessToken, "token_type": "bearer"}