from pymongo import MongoClient

cl = MongoClient('localhost', 27017)

db = cl.my_database
co = db.my_collection

#co.insert_one({"test":3})
for data in co.find():
    print(data)