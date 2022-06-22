from pydantic import BaseModel, Field
from typing import Union
from utils import PydanticObjectId
class TestResults(BaseModel):
  userId: Union[str, None] = None
  testType: Union[str, None] = None
  testTime: Union[int, None] = None
  inputWords: list[str] = []
  generatedWords: list[str] = []
  acc: Union[float, None] = None
  rawWpm: Union[float, None] = None
  wpm: Union[float, None] = None
  correctWords: Union[float, None] = None
class TestCreate(TestResults):
  id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
