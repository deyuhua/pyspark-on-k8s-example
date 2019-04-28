FROM spark-py:spark-docker

MAINTAINER HUADEYU huadeyu@kingsoft.com
WORKDIR /mnt

COPY . /mnt

RUN python3 setup.py install
