FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Installer netcat pour wait-for-postgres.sh
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

EXPOSE 5001

CMD ["/wait-for-postgres.sh", "python", "app.py"]

