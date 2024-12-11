@echo off

echo Pulling latest Docker images...
docker-compose pull

echo Building and running the application interactively...
docker-compose run --rm my-application
pause
