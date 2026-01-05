# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
# gcc and libpq-dev are often needed for building python packages like psycopg2 (if using non-binary)
# binutils, libproj-dev, gdal-bin are needed for PostGIS/GeoDjango
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    binutils \
    libproj-dev \
    gdal-bin \
    && apt-get clean

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port (Internal container port)
EXPOSE 8000

# Default command (will be overridden in docker-compose for dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
