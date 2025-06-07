from fastapi import FastAPI
import uvicorn

from services.user_meta.routers import user_meta

app = FastAPI(docs_url="")


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


app.include_router(user_meta.router)

if __name__ == "__main__":
    uvicorn.run(
        "services.user_meta.main:app",
        port=8002,
        reload=True
    )