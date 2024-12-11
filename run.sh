#!/bin/bash

# Pull the latest version of Docker images if needed
docker-compose pull

# Build the Docker images
docker-compose build

# Run the application interactively
docker-compose run --rm my-application
