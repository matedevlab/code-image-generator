#!/bin/bash

# Check if SECRET_KEY is not set
if [ -z "$SECRET_KEY" ]; then
  echo "Generating a new secret key..."
  SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(16))')
fi

# Create config.py with SECRET_KEY
echo "SECRET_KEY = '$SECRET_KEY'" > /usr/src/app/config.py

# Start Gunicorn
exec gunicorn -b 0.0.0.0:5000 app:app
