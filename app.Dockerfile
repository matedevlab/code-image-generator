# Use a specific version of Playwright's official Docker image
FROM mcr.microsoft.com/playwright:v1.35.0-jammy

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make the script executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Install any needed packages specified in requirements-prod.txt
RUN python3 -m pip install --no-cache-dir -r requirements-prod.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the script as the entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
