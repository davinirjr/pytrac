FROM debian:stable
MAINTAINER Pirmin Tapken <pirmin.tapken@jimdo.com>
RUN apt-get update && apt-get install -y python2.6 python-virtualenv pandoc
RUN mkdir -p /home/pytrac/data
RUN virtualenv -p python2.6 /home/pytrac/venv
WORKDIR /home/pytrac/data
COPY ./requirements.txt /tmp/requirements.txt
RUN /home/pytrac/venv/bin/pip install -r /tmp/requirements.txt
ENTRYPOINT ["/home/pytrac/venv/bin/python", "./setup.py", "test"]
