FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY wait-for-postgres.sh /wait-for-postgres.sh
COPY wait-for-kafka.sh /wait-for-kafka.sh
RUN chmod +x /wait-for-postgres.sh /wait-for-kafka.sh

EXPOSE 5003

CMD ["/bin/sh", "-c", "/wait-for-postgres.sh /wait-for-kafka.sh python app.py"]

