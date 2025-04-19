import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wassimos@postgres-user:5432/userdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"

