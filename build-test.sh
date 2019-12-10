#! /bin/sh

docker build -t python-test -f TestDockerfile .
test_volume_exists=$(docker volume ls | grep python-test-volume)
if [ -z "$test_volume_exists" ]; then
  docker volume create python-test-volume
fi

mkdir output 2> /dev/null
directory_coverage_exists=$(ls | grep output/coverage)
directory_tests_exists=$(ls | grep output/tests)
directory_flake8_exists=$(ls | grep output/flake8)
if [ -z "$directory_coverage_exists" ]; then
  mkdir output/coverage
fi
if [ -z "$directory_flake8_exists" ]; then
  mkdir output/flake8
fi
if [ -z "$directory_tests_exists" ]; then
  mkdir output/tests
fi

docker run --network='host' \
           -v $(pwd)/output/:/peacemakr/python/output/ \
           python-test

firefox output/*/index.html output/tests/*.html
