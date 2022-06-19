from pydantic import BaseModel
from bson import ObjectId
from typing import List

class TestResults(BaseModel):
  userId: ObjectId
  testType: str
  testTime: int
  inputWords: List[str] = []
  generatedWords: List[str] = []

