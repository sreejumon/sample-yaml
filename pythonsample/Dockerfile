FROM ubuntu:14.04

RUN apt-get update && apt-get -y install python3.4 \
python3-pip \
dnsutils

RUN pip3 install redis

COPY . /opt/source-code

ENTRYPOINT python3 /opt/source-code/main.py
