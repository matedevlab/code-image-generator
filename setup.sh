#!/bin/bash

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Install Playwright browser binaries
python3 -m playwright install

# Generate a secret key and write it to .env file
echo "SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(16))')" > .env