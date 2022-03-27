FROM python:3.10-alpine3.15
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend/
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .

