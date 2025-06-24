# slim Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    sysstat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY app/main.py .


RUN chmod -R 755 /app

EXPOSE 5000

# Use Gunicorn for production deployment server.
CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:5000", "--workers", "4", "--timeout", "120"]