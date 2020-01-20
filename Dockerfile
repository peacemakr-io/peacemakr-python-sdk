FROM danielhuang37/peacemakr-pycmakessl:latest as builder

WORKDIR /peacemakr/python
ADD requirements.txt \
    examples/example.py \
    setup.py /peacemakr/python/

ADD peacemakr_sdk ./peacemakr_sdk/

RUN bash && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && python setup.py install

FROM python:3.7.4-alpine

WORKDIR /peacemakr/python
COPY --from=builder /peacemakr/python .
COPY --from=builder /usr/lib /usr/lib
COPY --from=builder /usr/local/lib /usr/local/lib

ENV LD_LIBRARY_PATH=/usr/local/lib
CMD python example.py
