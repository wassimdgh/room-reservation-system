import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wassimos@postgres-salle:5432/salledb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
