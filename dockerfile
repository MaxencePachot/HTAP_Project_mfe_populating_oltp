# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Copy the entire app directory into the container
COPY . .

# Set MySQL environment variables
ENV MYSQL_ROOT_PASSWORD=secret
ENV MYSQL_DATABASE=E_COMMERCE
ENV MYSQL_ROOT_HOST=localhost

EXPOSE 8000 8089

# Start uvicorn and locust in separate threads
CMD ["bash", "-c", "uvicorn fast_api:app --host 0.0.0.0 --port 8000 & locust -f mysql_clients_insert_data_fastapi_locust.py --host http://localhost:8000"]

