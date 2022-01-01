#!/bin/sh -ex

mypy firestorefastapi
flake8 firestorefastapi tests
black firestorefastapi tests --check
isort firestorefastapi tests scripts --check-only
