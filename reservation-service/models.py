from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # Add this import at the top

db = SQLAlchemy()

class Reservation(db.Model):
    __tablename__ = 'reservationservice'  # Table name in the shared database
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    salle_id = db.Column(db.Integer, nullable=False)
    date_reservation = db.Column(db.DateTime, default=datetime.utcnow)

