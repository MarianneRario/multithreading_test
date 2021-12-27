from flask_pymongo import MongoClient
import certifi


# SSL CERTIFICATE
ca = certifi.where()
cluster = MongoClient(
    "mongodb+srv://rariom:marianne07@cluster0.20txl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    tlsCAFile=ca)
# FETCHING DATABASE
db = cluster["facebook"]
# COLLECTION NAME (OR TABLE NAME FOR SQL)
collection = db["accounts"]

# for index, result in enumerate(collection.find({"accounts1.group": "1"})):
#     account = result["accounts1"]
#     print(account[index])
ctr = 0
while ctr < 3:
    for result in collection.find({"accounts1.group": "1"}):
        account = result["accounts1"]
        print(account[ctr]["name"])
    ctr += 1