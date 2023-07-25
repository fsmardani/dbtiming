from pymongo import mongo_client
import pymongo
import os

client = mongo_client.MongoClient()
print('Connected to MongoDB...')


def init_mongo():
    mongo_db = client[os.getenv("MONGO_URI")]
    return mongo_db
# Comments = mongo_db.comments



