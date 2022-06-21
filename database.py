import motor.motor_asyncio
import os

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URL"))

database = client.befaster