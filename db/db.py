import certifi
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL : str | None = os.environ.get("MONGO_DB")

client : AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URL, tlsCAFile =certifi.where())
database : AsyncIOMotorDatabase = client["ing_swii"]
collection : AsyncIOMotorCollection = database["usuarios"]