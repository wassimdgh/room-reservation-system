from flask import Flask, jsonify, request
from models import db, Reservation
from config import Config
from kafka import KafkaProducer
import json

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route("/reservations", methods=["POST"])
def create_reservation():
    data = request.get_json()
    if "user_id" not in data or "salle_id" not in data:
        return jsonify({"message": "Missing fields"}), 400

    reservation = Reservation(
        user_id=data["user_id"],
        salle_id=data["salle_id"],
        date_reservation=data.get("date_reservation", None)  # Optional field
    )
    db.session.add(reservation)
    db.session.commit()

    # Send a message to Kafka
    producer.send(Config.KAFKA_TOPIC, {
        "reservation_id": reservation.id,
        "user_id": reservation.user_id,
        "salle_id": reservation.salle_id
    })

    return jsonify({"message": "Réservation enregistrée"}), 201

@app.route("/reservations", methods=["GET"])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([
        {
            "id": r.id,
            "user_id": r.user_id,
            "salle_id": r.salle_id,
            "date_reservation": r.date_reservation.isoformat() if r.date_reservation else None
        } for r in reservations
    ])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5003)

