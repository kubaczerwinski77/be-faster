from pydantic import BaseModel, EmailStr, Field
from utils import PydanticObjectId
class UserBase(BaseModel):
  email: EmailStr
  username: str
  password: str

class UserCreate(UserBase):
  id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
  