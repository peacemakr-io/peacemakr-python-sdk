FROM python:3.7.4-alpine

RUN apk update && apk upgrade && apk add --no-cache git curl g++ gcc musl-dev libbsd-dev ca-certificates && update-ca-certificates

ADD requirements.txt \
    test-requirements.txt \
    examples/example.py \
    setup.py /app/

ADD peacemakr_sdk /app/peacemakr_sdk/

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install -r test-requirements.txt \
    && python setup.py install

CMD python example.py

