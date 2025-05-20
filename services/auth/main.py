from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.backend.mongo_db import init_mongo
from app.routers import auth
from app.routers import ecg
from app.routers import user_meta


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongo()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(ecg.router)
app.include_router(auth.router)
app.include_router(user_meta.router)
