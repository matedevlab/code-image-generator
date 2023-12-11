# Create image from code

The Code Image Generator is a web application that allows users to paste Python code, select a theme, and generate an image from the styled code snippet. This tool is perfect for developers who want to share their code in a visually appealing way.

## Prerequisites

- Python 3.10

## Setup Instructions

1. Navigate to the project directory in the terminal.
2. Run `./setup.sh` to set up the virtual environment, install dependencies, and generate a secret key in the `.env` file.
3. Activate the virtual environment with `source venv/bin/activate`.

## Running the Application

Run the application using the following command:
`gunicorn -k gevent -w 2 -b localhost:5000 application.app:app`

This command starts the Flask application with Gunicorn as the WSGI server.

## Usage

After starting the application, navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start using the Code Image Generator.

# Usage of the Pipeline

## Create Personal Access Token to access the GitHub API to create release

1. Generate Token:

   - Click on your profile in the top right corner
   - Click "Settings" -> "Developer settings" (the last in the list)
   - Then "Personal access tokens" -> "Tokens(classic)" -> "Generate new token(classic)"
   - Give a Note
   - Select the expiration time
   - Tick the "repo" box -> Generate token -> copy and save the token

2. Add the Token to GitHub Secrets:

   - Go to your GitHub repository.
   - Navigate to "Settings" > "Secrets and varibales" > "Actions".
   - Add "New repository secret" (e.g., RELEASE_PAT) and paste the Token.

## Creating and Configuring a Service Account in GCP

1. Create a Service Account:

   - Go to the Google Cloud Console.
   - Navigate to "IAM & Admin" > "Service Accounts".
   - Create a new service account with a descriptive name.

2. Assign Roles:

   - Assign the "Artifact Registry Administrator" role to this service account.

3. Create a JSON Key:

   - In the service account details, go to the "Keys" section.
   - Create a new key of type JSON. Download this key, as you will need it for your GitHub repository.

## Configuring GitHub Repository Secrets

1. Add the JSON Key to GitHub Secrets:

   - Go to your GitHub repository.
   - Navigate to "Settings" > "Secrets and varibales" > "Actions".
   - Add "New repository secret" (e.g., GCP_CREDENTIALS) and paste the content of the JSON key file you downloaded.

## Create Artifact Registry to store the docker images

1. Navigato to "Artifact Registry"
2. On the top of the page click the "+" sign to create new repository
3. Give a name
4. Format: Docker
5. Mode: Standard
6. Location type: Region (choose the closest to you)
7. Encryption: Google-managed encryption key
8. Cleanup policies: Dry run
9. Create

test2
