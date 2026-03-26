from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["research_search"]

collection = db["papers"]


def insert_papers(papers: list):
    collection.delete_many({}) 
    print("Old data deleted")
    
    if papers:
        collection.insert_many(papers)


def get_all_papers():
    papers = list(collection.find({}, {"_id": 0}))

    return papers