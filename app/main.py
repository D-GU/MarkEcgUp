from fastapi import FastAPI

from app.routers import auth
from app.routers import ecg

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(ecg.router)
app.include_router(auth.router)
