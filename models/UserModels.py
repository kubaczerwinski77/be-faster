from pydantic import BaseModel, EmailStr, Field
from utils import PydanticObjectId
from typing import Union
class UserBase(BaseModel):
  email: EmailStr
  username: str
  password: str
  disabled: Union[bool, None] = None

class UserCreate(UserBase):
  id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
  