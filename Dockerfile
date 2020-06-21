FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins

ENV num=2

ENTRYPOINT python -u main.py $num
