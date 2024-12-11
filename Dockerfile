FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

# Use environment variables to configure external service URLs
ENV SERVICE_URL http://service-host:port

# Run app.py when the container launches
CMD ["python", "app.py"]
