from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from mongo import Mongo
from rabbit import Rabbit

# init app
app = Flask(__name__)

@app.route("/")
def index():
    return "duohong"

# signup
@app.route("/signup")
def signup():
    username = request.josn["username"]
    password = request.josn["password"]
    hashed_password = generate_password_hash(password, method="sha256")
    return "Created a user"

# signin
@app.route("/signin")
def signin():
    Mongo.save_new_user("created by duohong")
    Rabbit.send_new_user("created by duohong")
    return "Created a user"

# test
@app.route("/test")
def test():
    return jsonify({"Duohong" : datetime.datetime.utcnow()})

# run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
