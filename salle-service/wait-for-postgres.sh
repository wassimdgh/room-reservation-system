#!/bin/bash

# Arguments: $1 = Host, $2 = Port, $3 = Command to run (e.g., python app.py)
HOST=$1
PORT=$2
CMD="${@:3}"

echo "⏳ Waiting for $HOST to be ready on port $PORT..."

# Use netcat (nc) to check if the port is open on the given host
while ! nc -z "$HOST" "$PORT"; do
  sleep 1
done

echo "✅ $HOST is up - launching app"

# Execute the provided command (e.g., python app.py)
exec $CMD

