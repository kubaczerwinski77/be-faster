from bson.objectid import ObjectId as BsonObjectId
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verifyPassword(plainPassword, hashedPassword):
  return pwdContext.verify(plainPassword, hashedPassword)

def getPasswordHash(password):
  return pwdContext.hash(password)

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="token")
