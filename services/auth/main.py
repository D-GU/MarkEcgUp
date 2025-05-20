from fastapi import FastAPI

from .routers import auth

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(auth.router)
