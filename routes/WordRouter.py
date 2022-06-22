from fastapi import APIRouter, HTTPException
from controllers.WordController import Word
from models.WordModels import WordCreate

router = APIRouter(
  prefix="/words",
  tags=["words"]
)

initWord = Word()

@router.get("/{id}", response_model=WordCreate)
async def get_word_by_id(id):
  response = await initWord.fetch_word_by_id(id)
  if response:
    return response
  raise HTTPException(404, f"There is no user with id {id}")

@router.get("/", tags=["words"])
async def get_all_words():
  response = await initWord.fetch_all_words()
  return response
