from database import database
from models.WordModels import WordBase
import asyncio

# create array of words
lines = []
with open("/Users/kubaczerwinski77/Desktop/studies/sem-let-2021-22/skryptowe/be-faster/words.txt", 'r') as f:
  lines = f.readlines()

# remove additional characters
wordList = list(map(lambda s : s.strip(), lines))

# connect with db
collection = database.words

# each letter gets the row number
row = [2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3]
rightHand = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']
leftHand = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']

# difficulty function
def calcDifficulty(word: str):

  n = len(word)
  diffpts = 1

  if n > 1:  
    for i in range(1, n):
      # add point if you need to change the row
      if(row[ord(word[i]) - ord('a')] != row[ord(word[i - 1]) - ord('a')]):
        diffpts += 1

      # add extra points if next letter is written by the same hand
      if word[i - 1] in rightHand and word[i] in rightHand:
        diffpts += 1

      if word[i - 1] in leftHand and word[i] in leftHand:
        diffpts += 1

  return diffpts

# create method that adds words to db
async def createWord(word: str, difficulty):
  await collection.insert_one(WordBase(word=word, difficulty=difficulty).dict())

# add all words
async def createWordSet():
  for word in wordList:
    await createWord(word, calcDifficulty(word))

asyncio.run(createWordSet())