# code-image-generator
You can paste the code and it will generate you an image

## Steps

1. Run setup.sh to create the virtual environment and download the dependencies
   - ./setup.sh


2. Activate the virtual environment
   - source venv/bin/activate

3. Create a config.py file in the root directory
4. Create a secret key in the terminal: "python -c 'import secrets; print(secrets.token_hex(16))'"
5. Paste the generated secret key into the config.py like this: "SECRET_KEY = 'your_secret_key'"