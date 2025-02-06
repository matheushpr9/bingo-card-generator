FROM python:alpine3.21

WORKDIR /app
COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt