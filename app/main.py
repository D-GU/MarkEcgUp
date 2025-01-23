from fastapi import FastAPI

from app.routers import ecg

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome"}

app.include_router(ecg.router)
