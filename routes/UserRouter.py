from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.UserModels import UserCreate, UserBase
from controllers.UserController import User
from utils import getPasswordHash, oauth2Scheme, verifyPassword

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

initUser = User()

@router.get("/", tags=["users"])
async def get_users():
  response = await initUser.fetch_all_users()
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
    user = await initUser.fetch_one_user_by_username(token) 
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
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

@router.post("/token")
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    userDict = await initUser.fetch_one_user_by_username(formData.username)
    if not userDict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserCreate(**userDict)
    if not verifyPassword(formData.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}