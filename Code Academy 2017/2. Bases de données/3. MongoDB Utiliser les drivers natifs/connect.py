#!/usr/bin/env python3

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("127.0.0.1", 27017)

db = client.LXF
sampleData = db.sampleData
someData = db.someData
item = sampleData.find()
itemList = someData.find()

# Crud Method
someData.insert_one({"username": "meta", "code": 10, "time": datetime.now(), "n": 7777})

print(someData.find({"username": "meta"}))
someData.delete_many({"username": "meta"})
someData.insert_one({"username": "meta", "code": 10, "time": datetime.now(), "n": 7777})
print(someData.find({"username": "meta"}))
someData.update_one({"username": "meta"}, {"$set": {"n": 9999}})
print(someData.find({"username": "meta"}))

for el in item:
    print(el)

for el in itemList:
    print(el)
