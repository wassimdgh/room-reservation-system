#!/bin/sh

echo "⏳ Waiting for postgres-user to be ready..."

while ! nc -z postgres-user 5432; do
  sleep 1
done

echo "✅ Postgres-user is up - launching app"
exec "$@"
