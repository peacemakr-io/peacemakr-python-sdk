FROM python:3.7.4-alpine

RUN apk update && apk upgrade && apk add --no-cache bash make git curl g++ perl gcc musl-dev libbsd-dev ca-certificates && update-ca-certificates

RUN wget "https://www.openssl.org/source/openssl-1.1.1d.tar.gz" && tar -zxf openssl-1.1.1d.tar.gz && cd openssl-1.1.1d && ./config && make && make install
RUN wget "https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0.tar.gz" && tar -zxf cmake-3.16.0.tar.gz && cd cmake-3.16.0 && ./bootstrap && make && make install

WORKDIR /peacemakr
ADD requirements.txt \
    test-requirements.txt \
    examples/example.py \
    setup.py /peacemakr/python/

ADD peacemakr_sdk /peacemakr/python/peacemakr_sdk/

WORKDIR /peacemakr/python

RUN bash && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install -r test-requirements.txt \
    && python setup.py install

ENV LD_LIBRARY_PATH=/usr/local/lib
CMD python example.py
