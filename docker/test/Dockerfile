FROM python:3.8.5-slim

WORKDIR /api
COPY . /api

RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install -r requirements.txt

RUN pytest tests/v1 -s --cov=. --cov-fail-under 100 --log-cli-level ERROR
