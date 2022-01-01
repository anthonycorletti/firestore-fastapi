#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports firestorefastapi tests scripts

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place firestorefastapi tests scripts --exclude=__init__.py
black firestorefastapi tests scripts
isort firestorefastapi tests scripts
