from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

db = client["research_search"]

collection = db["papers"]


def insert_papers(papers: list):
    collection.delete_many({})

    if papers:
        collection.insert_many(papers)

    print("Fresh data inserted")

def get_all_papers():
    papers = list(collection.find({}, {"_id": 0}))

    return papers