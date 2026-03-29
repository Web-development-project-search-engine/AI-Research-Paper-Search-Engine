from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["research_search"]

collection = db["papers"]


def insert_papers(papers: list):
    for paper in papers:
        collection.update_one(
            {"id": paper["id"]},   # match by unique id
            {"$set": paper},
            upsert=True
        )
    
    print("Papers inserted/updated successfully")


def get_all_papers():
    papers = list(collection.find({}, {"_id": 0}))

    return papers