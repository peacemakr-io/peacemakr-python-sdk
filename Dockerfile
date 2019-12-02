FROM python:3.7.4-alpine

RUN apk update && apk upgrade && apk add --no-cache git curl g++ gcc musl-dev libbsd-dev ca-certificates && update-ca-certificates

WORKDIR /peacemakr
ADD requirements.txt \
    test-requirements.txt \
    examples/example.py \
    setup.py /peacemakr/python/
ADD peacemakr_sdk /peacemakr/python/peacemakr_sdk/

WORKDIR /peacemakr/python
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install -r test-requirements.txt \
    && python setup.py install

ENV LD_LIBRARY_PATH=/usr/local/lib
CMD python example.py
