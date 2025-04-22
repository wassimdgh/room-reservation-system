import os  # Add this import at the top

class Config:
    # Using the same database for salles
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wassimos@postgres-user:5432/systemreservationdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"

