from typing import Union
from xmlrpc.client import boolean
from pydantic import BaseModel, Field
from utils import PydanticObjectId

class TextReq(BaseModel):
  punctuation: Union[boolean, None] = None
  numbers: Union[boolean, None] = None
  mode: str
  diff: str
  words: Union[int, None] = None

class TextRes(BaseModel):
  wordArr: list[str]
