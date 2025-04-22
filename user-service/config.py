import os

class Config:
    # Using a single PostgreSQL database: systemreservationdb
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wassimos@postgres-user:5432/systemreservationdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"

