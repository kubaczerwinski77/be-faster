from bson.objectid import ObjectId
from models.UserModels import UserCreate, UserBase
from database import database
from utils import PydanticObjectId, getPasswordHash, verifyPassword
class User():
  def __init__(self) -> None:
    self.collection = database.users
    self.resultsCollection = database.results

  async def fetch_one_user_by_email(self, email):
    document = await self.collection.find_one({"email": email})
    return document

  async def fetch_one_user_by_username(self, username):
    document = await self.collection.find_one({"username": username})
    return document
  
  async def fetch_one_user_by_id(self, id):
    document = await self.collection.find_one({"_id": ObjectId(id)})
    return document
  
  async def fetch_all_users(self):
    users = []
    cursor = self.collection.find({})
    async for document in cursor:
      users.append(UserCreate(**document))
    return users

  async def create_user(self, user):
    document = user
    document["password"] = getPasswordHash(document["password"])
    await self.collection.insert_one(document)
    return document
  
  async def remove_user(self, id):
    exists = await self.collection.find_one({"_id": ObjectId(id)})
    if not exists:
      return False
    await self.collection.delete_one({"_id": ObjectId(id)})
    return True
  
  async def authenticateUser(self, username: str, password: str):
    user = await self.fetch_one_user_by_username(username)
    user = UserBase(**user)
    if not user:
      return False
    if not verifyPassword(password, user.password):
      return False
    return user
  
  async def fetch_stats_by_user_id(self, id):
    tests = []
    # FIX THIS OBJECT ID ISSUE
    cursor = self.resultsCollection.find({"userId": ObjectId(id)})
    async for doc in cursor:
      tests.append(doc)
    return tests