# SSL CERTIFICATE
import certifi
from flask_pymongo import MongoClient

ca = certifi.where()
# DATABASE CLOUD CONNECTION
cluster = MongoClient(
    "mongodb+srv://rariom:marianne07@cluster0.20txl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
# FETCHING DATABASE
db = cluster["facebook"]
# COLLECTION NAME (OR TABLE NAME FOR SQL)
user_engagement_collection = db["user_engagement"]


def add_user_engagement(filename, url, email, password):
    post = {
        "filename": filename + ".png",
        "url": url,
        "accounts": [{
            "email": email,
            "password": password}
        ]
    }
    # INSERT DATA IN DATABASE
    user_engagement_collection.insert_one(post)
