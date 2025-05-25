from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from services.ecg.backend.mongo_db import init_mongo
from services.ecg.routers import ecg


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongo()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(ecg.router)

if __name__ == "__main__":
    uvicorn.run(
        "services.ecg.main:app",
        port=8001,
        reload=True
    )