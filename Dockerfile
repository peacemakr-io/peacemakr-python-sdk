FROM python:3.7.4
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
