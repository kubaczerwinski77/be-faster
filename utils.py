from bson.objectid import ObjectId as BsonObjectId
from numpy import deprecate
from passlib.context import CryptContext

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
