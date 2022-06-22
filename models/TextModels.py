from typing import Union
from xmlrpc.client import boolean
from pydantic import BaseModel

class TextReq(BaseModel):
  punctuation: Union[boolean, None] = None
  numbers: Union[boolean, None] = None
  mode: str
  diff: str
  words: Union[int, None] = None

class TextRes(BaseModel):
  wordArr: list[str]
