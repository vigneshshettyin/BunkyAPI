# Use a lightweight Python image
FROM python:3.11-slim

# Set environment variables for production
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Install system dependencies required for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r ./config/prod.txt


# Collect static files for Django
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bunky.wsgi:application"]
