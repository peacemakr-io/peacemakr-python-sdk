#!/bin/sh

set -ex

# Pull the latest
docker pull gcr.io/peacekube/peacemakr-services:latest || true
docker pull gcr.io/peacekube/key-derivation-service:latest || true
docker pull danielhuang37/peacemakr-pycmakessl:latest || true

docker build -t peacemakr-python-sdk-test -f TestDockerfile --network=host .
