from flask import Flask, jsonify, request
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if "username" not in data or "email" not in data:
        return jsonify({"message": "Missing fields"}), 400

    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"username": u.username, "email": u.email} for u in users])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5001)

