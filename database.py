from models.model import User
import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.befaster
collection = database.users

async def fetch_one_user(id):
  document = await collection.find_one({"_id": ObjectId(id)})
  return document

async def fetch_all_users():
  users = []
  cursor = collection.find({})
  async for document in cursor:
    users.append(User(**document))
  return users

async def create_user(user):
  document = user
  result = await collection.insert_one(document)
  return document

async def remove_user(id):
  await collection.delete_one({"_id": ObjectId(id)})
  return True