# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make sure bash is installed
RUN apt-get update && apt-get install -y bash

# Run the script when the container launches
ENTRYPOINT ["python", "fair_billing.py"]
