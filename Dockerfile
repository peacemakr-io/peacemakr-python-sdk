FROM python:3.7.4
WORKDIR /app
COPY ./requierments.txt /app
RUN pip install -r requierments.txt
