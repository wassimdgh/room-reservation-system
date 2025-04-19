#!/bin/sh

echo "⏳ Waiting for postgres-salle to be ready..."

while ! nc -z postgres-salle 5432; do
  sleep 1
done

echo "✅ Postgres-salle is up - launching app"
exec "$@"
