import time
from fastapi import FastAPI
from app.databases.mongodb import init_mongo
# from databases.mysql import init_mysql

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World ha"}


@app.get("/init")
async def root():
    return {"message": "Hello World ha"}

