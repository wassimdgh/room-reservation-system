import os

class Config:
    # Connexion à la base PostgreSQL via le nom du service Docker
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wassimos@postgres-reservation:5432/reservationdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clé secrète pour les tokens
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"

    # Connexion à Kafka via le nom du service Docker
    KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'
    KAFKA_TOPIC = 'reservation-topic'

