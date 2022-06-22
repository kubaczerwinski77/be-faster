from database import database
from bson.objectid import ObjectId

class TestResults():
  def __init__(self) -> None:
    self.collection = database.results

  async def remove_result(self, id):
    exists = await self.collection.find_one({"_id": ObjectId(id)})
    if not exists:
      return False
    await self.collection.delete_one({"_id": ObjectId(id)})
    return True

  async def create_test_results(self, testResults): 
    document = testResults

    # extract both texts
    generatedText = document["generatedWords"]
    userInput = document["inputWords"]

    # make variables that will count parameters
    correctWords = 0
    allLetters = 0
    correctLetters = 0

    # iterate and compare with generated text
    for i in range(0, len(userInput)):
      if userInput[i] == generatedText[i]:
        correctWords += 1
      # dont forget about space between words
      allLetters += len(userInput[i])
      for j in range (0, len(userInput[i])):
        if userInput[i][j] == generatedText[i][j]:
          correctLetters += 1

    # create overall results | normalize to 60 seconds
    acc = correctLetters / allLetters * 100
    wpm = correctLetters / 5 * (60 / document["testTime"])
    rawWpm = allLetters / 5 * (60 / document["testTime"])

    # replace document props with the calculated ones
    document["acc"] = acc
    document["wpm"] = wpm
    document["rawWpm"] = rawWpm
    document["correctWords"] = correctWords

    await self.collection.insert_one(document)
    return document
