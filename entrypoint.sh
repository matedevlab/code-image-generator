#!/bin/bash

# Check if SECRET_KEY is not set
if [ -z "$SECRET_KEY" ]; then
  echo "Generating a new secret key..."
  export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(16))')
fi

# Default to 2 workers if not set
: ${WORKERS:=2}

# Start Gunicorn
exec gunicorn -k gevent -w ${WORKERS} -b 0.0.0.0:5000 app:app
