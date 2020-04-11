import json

from pandelytics import search

if __name__ == "__main__":
    news = search.search("Twitter", "News")
    if news:
        print(json.dumps(news))
