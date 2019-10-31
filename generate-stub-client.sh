#!/bin/sh

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli:2.4.5 generate \
    -i local/peacemakr-services.yml \
    -l python \
    -o local

