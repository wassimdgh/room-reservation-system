from flask import Flask, jsonify, request
from models import db, Salle
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/salles", methods=["POST"])
def create_salle():
    data = request.get_json()
    if "nom" not in data or "capacite" not in data:
        return jsonify({"message": "Missing fields"}), 400

    nouvelle_salle = Salle(nom=data["nom"], capacite=data["capacite"])
    db.session.add(nouvelle_salle)
    db.session.commit()
    return jsonify({"message": "Salle ajoutée"}), 201

@app.route("/salles", methods=["GET"])
def get_salles():
    salles = Salle.query.all()
    return jsonify([{"nom": s.nom, "capacite": s.capacite} for s in salles])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables
    app.run(host="0.0.0.0", port=5002)  # Ensure it listens on all addresses and port 5002

