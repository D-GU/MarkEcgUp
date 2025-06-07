import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.ecgs import ECG

MONGO_URL = os.getenv(
    "MONGODB_URL",
    default="mongodb://localhost:27017"
)

MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", default="ecg")


async def init_mongo():
    client = AsyncIOMotorClient(MONGO_URL)
    await init_beanie(database=client[MONGO_DB_NAME], document_models=[ECG])
