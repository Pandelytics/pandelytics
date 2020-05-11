from pandelytics import search
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    news = search.search("jhu", "Data")
    return news