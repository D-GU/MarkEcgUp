import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from services.auth.routers import auth

load_dotenv(".env")

ECG_ADDRESS = os.getenv("ECG_ADDRESS")
USER_META_ADDRESS = os.getenv("USER_META_ADDRESS")

origins = [
    "http://127.0.0.1:8001",
    "http://localhost:8001",
    "http://127.0.0.1:8002",
    "http://localhost:8002",
    "http://127.0.0.1:8080",
    "http://localhost:8080"
]

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(
        "services.auth.main:app",
        port=8000,
        reload=True
    )
