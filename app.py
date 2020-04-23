import json

from pandelytics import search

if __name__ == "__main__":
    news = search.search("jhu", "Data")
    if news:
        print(json.dumps(news, indent=4))
