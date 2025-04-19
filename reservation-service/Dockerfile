FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Installer netcat pour wait-for scripts
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier les scripts d'attente
COPY wait-for-postgres.sh /wait-for-postgres.sh
COPY wait-for-kafka.sh /wait-for-kafka.sh
RUN chmod +x /wait-for-postgres.sh /wait-for-kafka.sh

EXPOSE 5003

# Lancer le service après attente de Postgres + Kafka
CMD ["/bin/sh", "-c", "/wait-for-postgres.sh /wait-for-kafka.sh python app.py"]

