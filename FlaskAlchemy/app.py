from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route("/")
def index():
    return "duohong"

# database
# easy to switch to ms sql server here.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# user class/model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    hashed_password = db.Column(db.String(128))
     
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password

# user schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username")

# init schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)

# signup
@app.route("/signup")
def signup():
    username = request.josn["username"]
    password = request.josn["password"]
    hashed_password = generate_password_hash(password, method="sha256")
    new_user = User(username, hashed_password)
    try: 
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({"message" : "Database error!"}), 500

    token = jwt.encode({"id" : new_user.id, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, "MY_SECRET_KEY")
    return jsonify({"token" : token.decode("UTF-8")})

# signin
@app.route("/signin")
def signin():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=auth.username).first()
    if not user:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm="Login required!"'})

    if check_password_hash(user.hashed_password, auth.password):
        token = jwt.encode({"id" : user.id, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, "MY_SECRET_KEY")
        return jsonify({"token" : token.decode("UTF-8")})

    return make_response("Could not verify", 401, {"WWW-Authenticate" : 'Basic realm="Login required!"'})

# test
@app.route("/test")
def test():
    return jsonify({"Hello World!" : datetime.datetime.utcnow()})

# run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
