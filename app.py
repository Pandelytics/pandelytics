import json

from pandelytics import search
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    if __name__ == "__main__":
        news = search.search("jhu", "Data")
        if news:
            return news