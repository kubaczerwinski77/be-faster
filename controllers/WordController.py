from database import database
from bson.objectid import ObjectId

from models.WordModels import WordBase, WordCreate

class Word:
  def __init__(self) -> None:
    self.collection = database.words

  async def fetch_all_words(self):
    words = []
    cursor = self.collection.find({})
    async for document in cursor:
      words.append(WordCreate(**document))
    return words
    
  async def fetch_word_by_id(self, id):
    document = await self.collection.find_one({"_id": ObjectId(id)})
    return document
  
  async def remove_word(self, id):
    exists = await self.collection.find_one({"_id": ObjectId(id)})
    if not exists:
      return False
    await self.collection.delete_one({"_id": ObjectId(id)})
    return True