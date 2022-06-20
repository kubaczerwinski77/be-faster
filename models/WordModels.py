from pydantic import BaseModel, Field
from utils import PydanticObjectId

class WordBase(BaseModel):
  word: str
  difficulty: float

class WordCreate(WordBase):
  id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")