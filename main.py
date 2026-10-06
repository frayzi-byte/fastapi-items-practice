from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from routers import router

@asynccontextmanager
async def lifespan(app : FastAPI):
    await create_tables()
    print("Starting... Base Ready")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

@app.get("/")
def get_home():
    return {"message" : "Hello World!"}