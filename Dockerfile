FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins

ENV NUMBERS=2

ENTRYPOINT python -u main.py $NUMBERS
