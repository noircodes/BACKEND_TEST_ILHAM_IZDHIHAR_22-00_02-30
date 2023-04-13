from pymongo import MongoClient

conn = MongoClient()
db = conn["local"]
col = db["user"]