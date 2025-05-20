from contextlib import asynccontextmanager

from fastapi import FastAPI

from .backend.mongo_db import init_mongo
from .routers import ecg


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongo()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(ecg.router)
