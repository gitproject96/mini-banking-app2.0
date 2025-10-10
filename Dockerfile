# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for efficient caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose Flask port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV APP_VERSION=v1.0.0

# Run the application
CMD ["python", "app.py"]
