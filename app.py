import json

from pandelytics import search

def main():
    news = search.search("jhu", "Data")
    if news:
        print(json.dumps(news, indent=4))
