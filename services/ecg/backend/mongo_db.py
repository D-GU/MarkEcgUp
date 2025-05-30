import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.ecg import ECG

MONGO_URI = os.getenv(
    "MONGO_URL",
    default="mongodb://localhost:27017"
)

DB_NAME = os.getenv("MONGO_DB_NAME", default="ecg")


async def init_mongo():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client[DB_NAME], document_models=[ECG])
