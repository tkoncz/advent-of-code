FROM python:3.10.0-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update -y && apt-get install -y python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt
