#!/bin/bash

# Create a virtual environment named 'venv'
python3 -m venv venv

# Install dependencies from requirements.txt
venv/bin/pip3 install -r requirements.txt

# Install Playwright browser binaries
venv/bin/python3 -m playwright install

# Generate a secret key and write it to .env file
echo "SECRET_KEY=$(venv/bin/python -c 'import secrets; print(secrets.token_hex(16))')" > .env

# Append PYTHONPATH setting to the virtual environment activation script
echo "export PYTHONPATH=\$PYTHONPATH:$(pwd)" >> venv/bin/activate
