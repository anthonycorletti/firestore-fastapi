FROM python:3.8.5-slim

WORKDIR /api
COPY . /api

RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && python3 setup.py install

CMD gunicorn main:api -c gunicorn_config.py
