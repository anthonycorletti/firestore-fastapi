#!/bin/sh -e

gunicorn firestorefastapi.main:api -c firestorefastapi/gunicorn_config.py
