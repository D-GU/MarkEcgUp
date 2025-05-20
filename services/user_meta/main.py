from fastapi import FastAPI

from .routers import user_meta

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(user_meta.router)
