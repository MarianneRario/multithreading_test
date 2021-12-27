from datetime import datetime as dt
from flask import Flask, request, jsonify, make_response
from flask_pymongo import MongoClient
from functools import wraps
import certifi
import jwt
import datetime
import threading
import hashlib
import device1
import device2
import device3
import thread_counter

# SSL CERTIFICATE
ca = certifi.where()
# DATABASE CLOUD CONNECTION
cluster = MongoClient(
    "mongodb+srv://rariom:marianne07@cluster0.20txl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
# FETCHING DATABASE
db = cluster["facebook"]
# COLLECTION NAME (OR TABLE NAME FOR SQL)
collection = db["credentials"]

dbhex_password = ""
db_username = ""
for result in collection.find({"_id": "1"}):
    dbhex_password = result["password"]
    db_username = result["username"]


app = Flask(__name__, template_folder='template')
app.config["SECRET_KEY"] = "lu7ci8zi"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            return jsonify({"message ": "Token is missing"}), 403

        try:

            payload = token, app.config["SECRET_KEY"]
        except:
            return jsonify({"message ": "Token is invalid"}), 403

        return f(*args, **kwargs)

    return decorated


@app.route("/login", methods=["POST"])
@token_required
def main():
    # TIMER
    time_now = dt.now().minute
    # DATA FROM API
    dataDict = request.get_json()
    url = dataDict["url"]
    comment = dataDict["comment"]

    if thread_counter.thread_count == 0:
        threading.Thread(target=device1.main, args=(url, comment, time_now)).start()
    elif thread_counter.thread_count == 1:
        threading.Thread(target=device2.main, args=(url, comment, time_now)).start()
    elif thread_counter.thread_count == 2:
        threading.Thread(target=device3.main, args=(url, comment, time_now)).start()
    return {"Response": 200}


@app.route("/", methods=["POST"])
def protect():
    auth = request.authorization
    hex_pass = hashlib.sha256(auth.password.encode('utf-8')).hexdigest()

    if auth.username == db_username and hex_pass == dbhex_password:
        token = jwt.encode({
            "user": auth.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        },
            app.config["SECRET_KEY"])
        return jsonify({"token": token})

    return make_response("Could not verify", 401, {"WWW-Authenticate": "Basic realm=" 'Login Required'})


if __name__ == '__main__':
    app.debug = True
    app.run()
