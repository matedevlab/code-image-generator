# Create image from code

The Code Image Generator is a web application that allows users to paste Python code, select a theme, and generate an image from the styled code snippet. This tool is perfect for developers who want to share their code in a visually appealing way.

## Prerequisites

- Python 3.10
- Docker
- Docker Compose

## Setup Instructions

1. Navigate to the project directory in the terminal.
2. Run `./setup.sh` to set up the virtual environment, install dependencies, and generate a secret key in the `.env` file.
3. Activate the virtual environment with `source venv/bin/activate`.

## Running the Application

Run the application using the following command:
`gunicorn -k gevent -w 2 -b localhost:5000 application.app:app` or `docker-compose up --build -d`

## Usage

After starting the application, navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to start using the Code Image Generator.

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

   - Assign the "Artifact Registry Administrator", "Service Account Token Creator", "App Engine Admin", "Storage Object Admin", "Service Account User" role to this service account.

3. Create a JSON Key:

   - In the service account details, go to the "Keys" section.
   - Create a new key of type JSON. Download this key, as you will need it for your GitHub repository.

4. Add the JSON Key to GitHub Secrets:

   - Go to your GitHub repository.
   - Navigate to "Settings" > "Secrets and varibales" > "Actions".
   - Add "New repository secret" (e.g., GCP_SERVICE_ACCOUNT_KEY) and paste the content of the JSON key file you downloaded.

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

## Create a Cloud Storage Bucket to store the Terraform state file

1. Navigate to the Cloud Storage
2. Create Bucket
3. Choose a unique name
4. Select Region (whatevre you want)
5. Set Standard as storage class
6. Enable "Enforce public access prevention on this bucket" and select Uniform
7. Select Object versioning and set "Max. number of versions per object" to 1 and "Expire noncurrent versions after" to 7

## Create App Engine application

1. Select the region
2. Select the already created service account

## Set Google service account json key for local running the infrastructure

1. Open .bashrc or .zshrc file: `nano ~/.bashrc` or `nano ~/.zshrc`
2. Add the Export command: `export GOOGLE_APPLICATION_CREDENTIALS="/path/of/your/service-account-key.json"`
3. Reload the Zsh/Bash configuration: `source ~/.zshrc` or `source ~/.bashrc`
4. Now you can run `terraform init` from the infrastructure folder to initialize the GCS backend

## Enable Google cloud APIs

1. Enable "Artifact Registry API"
2. Enable "Storage Insights API"
3. Enable "App Engine Admin API"
4. Enable "Google App Engine Flexible Environment"

test3
