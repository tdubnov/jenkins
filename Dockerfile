FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins

ENV NUMBER=10

ENTRYPOINT python -u main.py $NUMBER