FROM spark-py:spark-docker

MAINTAINER HUADEYU deyuhua@gmail.com
WORKDIR /mnt

COPY . /mnt

RUN python3 setup.py install
