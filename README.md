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
`gunicorn -k gevent -w 1 -b localhost:5000 app:app`

This command starts the Flask application with Gunicorn as the WSGI server.

## Usage

After starting the application, navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start using the Code Image Generator.
