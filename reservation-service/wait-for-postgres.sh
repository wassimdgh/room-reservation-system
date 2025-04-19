#!/bin/sh

echo "⏳ Waiting for postgres-reservation to be ready..."

while ! nc -z postgres-reservation 5432; do
  sleep 1
done

echo "✅ Postgres-reservation is up - launching app"
exec "$@"

