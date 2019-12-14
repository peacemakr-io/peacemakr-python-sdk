#!/bin/sh

set -ex

# Setup credentials
$(aws ecr get-login --no-include-email --region us-east-2) || true

# Pull the latest
docker pull 716293438869.dkr.ecr.us-east-2.amazonaws.com/peacemakr-services:latest || true
docker pull 716293438869.dkr.ecr.us-east-2.amazonaws.com/key-derivation-service:latest || true
docker pull danielhuang37/peacemakr-pycmakessl:latest || true

docker build -t peacemakr-python-sdk-test -f TestDockerfile --network=host .

