#!/bin/sh -e

IMAGE_VERSION=${IMAGE_VERSION:=latest}
docker push "anthonycorletti/firestorefastapi:${IMAGE_VERSION}"
