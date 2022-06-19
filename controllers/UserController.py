from bson.objectid import ObjectId
from models.UserModels import UserCreate
from database import database

class User():
  def __init__(self) -> None:
    self.collection = database.users

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
    print(users)
    return users

  async def create_user(self, user):
    document = user
    await self.collection.insert_one(document)
    return document
  
  async def remove_user(self, id):
    await self.collection.delete_one({"_id": ObjectId(id)})
    return True