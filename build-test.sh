#!/bin/sh

set -ex

# Setup credentials
$(aws ecr get-login --no-include-email --region us-east-2) || true

# Pull the latest
docker pull 716293438869.dkr.ecr.us-east-2.amazonaws.com/peacemakr-services:latest || true
docker pull 716293438869.dkr.ecr.us-east-2.amazonaws.com/key-derivation-service:latest || true
docker pull danielhuang37/peacemakr-pycmakessl:latest || true

docker build -t peacemakr-python-sdk-test -f TestDockerfile --network=host .
# test_volume_exists=$(docker volume ls | grep python-test-volume)
# if [ -z "$test_volume_exists" ]; then
#   docker volume create python-test-volume
# fi

# mkdir output 2> /dev/null
# directory_coverage_exists=$(ls | grep output/coverage)
# directory_tests_exists=$(ls | grep output/tests)
# directory_flake8_exists=$(ls | grep output/flake8)
# if [ -z "$directory_coverage_exists" ]; then
#   mkdir output/coverage
# fi
# if [ -z "$directory_flake8_exists" ]; then
#   mkdir output/flake8
# fi
# if [ -z "$directory_tests_exists" ]; then
#   mkdir output/tests
# fi

# docker run --network='host' \
#            -v $(pwd)/output/:/peacemakr/python/output/ \
#            peacemakr-python-sdk-test

