from pymongo import MongoClient
import uuid
import threading
import cp3
import thread_counter
import discord_webhook
import certifi
import user_engagement

# SSL CERTIFICATE
ca = certifi.where()
# DATABASE CLOUD CONNECTION
cluster = MongoClient(
    "mongodb+srv://rariom:marianne07@cluster0.20txl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
# FETCHING DATABASE
db = cluster["facebook"]
# COLLECTION NAME (OR TABLE NAME FOR SQL)
collection = db["accounts"]
# FETCH THE ACCOUNTS:3 OBJECTS ARRAY
a3 = {"accounts3.group": "3"}
# GLOBAL COUNTER
ctr = 0
# TO LOCK THE THREAD
lock = threading.Lock()
# COMMENT NUMBER
account_num = 0


# FUNCTION QUERYING ACCOUNTS OBJECT(PER ARRAY)
def arr(account_arr):
    cursor = collection.find(account_arr)
    return cursor


# CHECK IF YOU RECENTLY USE THE ACCOUNT
def allowUse(accntTimestamp, time_now, accnt_url, url):
    currentTimestamp = max(time_now, accntTimestamp)
    pastAccountTimestamp = min(time_now, accntTimestamp)
    cTime = currentTimestamp - pastAccountTimestamp
    # IF THE ACCOUNT HAS NOT BEEN USE FOR 5 MINUTES, USE THE ACCOUNT (RETURN TRUE)
    # 5 MINS
    timeTheAccountShouldNotBeUse = 2
    # MEANING MATAGAL NANG STAGNANT ANG ACCOUNT
    if accnt_url != url:
        return True
    elif cTime > timeTheAccountShouldNotBeUse:
        return True


def worker(acc, fnc, accnt_arr, url, comment, time_now):
    global ctr
    global account_num

    if ctr < 2:
        for key in fnc(accnt_arr):
            account = key[acc]
            email = account[ctr]["email"]
            password = account[ctr]["password"]
            account_timestamp = account[ctr]["timestamp"]
            accnt_url = account[ctr]["url"]

            ctr += 1
            if allowUse(account_timestamp, time_now, accnt_url, url):
                worker3_id = str(uuid.uuid4())[:8]
                print("Worker id: ", worker3_id, " is working...")
                print(password, " next...")

                lock.acquire()
                thread_counter.thread_count = 0
                account_num += 1
                print(password, " is logging in...")
                print(password, " is currently in use...")

                # UPDATE URL
                newURL = collection.update_one({"accounts3.email": email},
                                               {"$set": {"accounts3.$.url": url}})

                newTimestamp = collection.update_one({"accounts3.email": email},
                                                     {"$set": {"accounts3.$.timestamp": time_now}})
                cp3.login(url, email, password)
                filename = str(uuid.uuid4())[:8]
                cp3.comment(comment, filename)
                img_url = "http://127.0.0.1:5000/static/img/" + filename + ".png"
                webhook_url_extension = "/static/img/" + filename + ".png"
                discord_webhook.webhook(img_url, worker3_id, webhook_url_extension)
                # ADD IN user_engagement collection
                user_engagement.add_user_engagement(filename, url, email, password)
                print(password, " is logged out")
                lock.release()
            else:
                print(password, " is not yet allowed to use")
    else:
        print("All accounts were exhausted from device 3...returning to the first account")
        ctr = 0


def main(url, comment, time_now):
    worker("accounts3", arr, a3, url, comment, time_now)
