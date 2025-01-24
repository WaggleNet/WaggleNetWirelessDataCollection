from pymongo import MongoClient

client = MongoClient("mongodb://44.211.45.178/27017")

db = client.hiveData

print(db.list_collection_names())
