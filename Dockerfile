# slim Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app/ ./app/
COPY app/main.py .


EXPOSE 5000

# Use Gunicorn for production WSGI serving
CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:5000"]
