FROM python:3.11-alpine

WORKDIR /app

COPY . .

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

