from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from ..models.ecg import ECG

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "ecg"

async def init_mongo():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client[DB_NAME], document_models=[ECG])

