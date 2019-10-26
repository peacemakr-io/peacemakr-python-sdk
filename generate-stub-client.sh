#!/bin/sh

rm -rf src/test/java/io/peacemakr/crypto/swagger || true

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli:2.4.5 generate \
    -i local/peacemakr-services.yml \
    -l python \
    --api-package io.peacemakr.crypto.swagger.client.api \

