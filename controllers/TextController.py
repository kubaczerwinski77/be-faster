from database import database
from bson.objectid import ObjectId
from models.TextModels import TextRes
from utils import DEFAULT_NUMBER_OF_WORDS
import random
import pymongo

class Text():
  def __init__(self) -> None:
    self.collection = database.words
    self.punctuation = [",", "?", "!", ".", ":", ";"]
    self.textCollection = database.texts
  
  async def fetch_text_by_id(self, id):
    document = await self.textCollection.find_one({"_id": ObjectId(id)})
    return document

  async def create_text(self, params):
    # find easiest and hardest word in db
    easiestWord = await self.collection.find_one({}, sort=[("difficulty", pymongo.ASCENDING)])
    hardestWord = await self.collection.find_one({}, sort=[("difficulty", pymongo.DESCENDING)])

    # set lowest and highest difficulty
    diff0 = easiestWord["difficulty"]
    diff1 = hardestWord["difficulty"]
    diff05 = (diff1 - diff0) / 2
    diff025 = diff05 / 2
    diff075 = diff05 * 1.5

    if params.diff == "easy":
      words = self.collection.aggregate([
        {
          "$match": {
            "difficulty": {
              "$lte": diff05,
            }
          }
        }
      ])
    elif params.diff == "hard":
      words = self.collection.aggregate([
        {
          "$match": {
            "difficulty": {
              "$gte": diff05,
            }
          }
        }
      ])
    else:
      words = self.collection.aggregate([
        {
          "$match": {
            "difficulty": {
              "$gte": diff025,
              "$lte": diff075,
            }
          }
        }
      ])

    allWords = []

    # I CANNOT IMPORT CONSTANT FROM UTILS
    async for word in words:
        newWord = word["word"]
        if params.numbers and random.uniform(0, 1) < 0.2:
          allWords.append(str(random.randint(0, 100)))
        if params.punctuation and random.uniform(0, 1) < 0.4:
          newWord += self.punctuation[random.randint(0, len(self.punctuation) - 1)]
        if params.punctuation and random.uniform(0, 1) < 0.2:
          newWord = newWord.capitalize()
        allWords.append(newWord)

    # choose 50 random words
    choosen = random.choices(allWords, k=DEFAULT_NUMBER_OF_WORDS)

    document = {
      "wordArr": choosen,
      "punctuation": params.punctuation,
      "numbers": params.numbers,
      "diff": params.diff,
    }

    await self.textCollection.insert_one(document)

    return TextRes(**document)

  async def remove_text(self, id):
    exists = await self.collection.find_one({"_id": ObjectId(id)})
    if not exists:
      return False
    await self.collection.delete_one({"_id": ObjectId(id)})
    return True