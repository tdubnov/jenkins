FROM python:3.6-jessie

ADD . /jenkins
WORKDIR /jenkins

ENV urls=https://www.html.am/templates/downloads/bryantsmith/greenblade/

ENTRYPOINT python -u url.py $urls