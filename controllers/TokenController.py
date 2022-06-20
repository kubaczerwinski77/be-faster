from typing import Union
from datetime import datetime, timedelta
from jose import jwt
import os

def createAccessToken(data: dict, expiresDelta: Union[timedelta, None] = None):
  toEncode = data.copy()
  if expiresDelta:
      expire = datetime.utcnow() + expiresDelta
  else:
      expire = datetime.utcnow() + timedelta(minutes=15)
  toEncode.update({"exp": expire})
  encodedJWT = jwt.encode(toEncode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
  return encodedJWT