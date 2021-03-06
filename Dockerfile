FROM python:3.7.4-alpine as builder

RUN apk update && apk upgrade && \
    apk add --no-cache bash make git curl g++ perl gcc musl-dev libbsd-dev ca-certificates && \
    update-ca-certificates

RUN wget "https://www.openssl.org/source/openssl-1.1.1d.tar.gz" && \
    tar -zxf openssl-1.1.1d.tar.gz && cd openssl-1.1.1d && \
    ./config && make && make install && \
    cd / && rm -rf openssl-1.1.1d && rm openssl-1.1.1d.tar.gz

RUN wget "https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0.tar.gz" && \
    tar -zxf cmake-3.16.0.tar.gz && cd cmake-3.16.0 && \
    ./bootstrap && make && make install && \
    cd / && rm -rf cmake-3.16.0 && rm cmake-3.16.0.tar.gz

WORKDIR /peacemakr/python
ADD requirements.txt \
    test-requirements.txt \
    examples/example.py \
    setup.py /peacemakr/python/
ADD peacemakr /peacemakr/python/peacemakr/
RUN bash && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && python setup.py install

FROM python:3.7.4-alpine
COPY --from=builder /peacemakr/python /peacemakr/python
COPY --from=builder /usr/lib /usr/lib
COPY --from=builder /usr/local/lib /usr/local/lib
ENV LD_LIBRARY_PATH=/usr/local/lib
WORKDIR /peacemakr/python
CMD python example.py
