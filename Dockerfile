# Use a lightweight base image
FROM python:3.11-slim

# Environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=False

# Set the working directory
WORKDIR /app

# Install only necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first for dependency installation
COPY ./config/prod.txt /app/config/prod.txt
COPY ./config/base.txt /app/config/base.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/config/prod.txt

# Copy the rest of the application code
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application's port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8008", "bunky.wsgi:application"]