from pydantic import BaseModel, EmailStr, Field
from utils import PydanticObjectId
class UserBase(BaseModel):
  email: EmailStr

class UserCreate(UserBase):
  id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
  username: str
  password: str 