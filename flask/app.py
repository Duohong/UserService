from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import rabbit

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
    return "Created a user"

# test
@app.route("/test")
def test():
    return jsonify({"Duohong" : datetime.datetime.utcnow()})

# run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
