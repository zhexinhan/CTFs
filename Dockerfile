FROM centos:centos7

RUN yum update -y

RUN yum install -y file wget ImageMagick-devel

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u python36u-pip java-1.8.0-openjdk-devel && \
    pip3.6 install --upgrade pip

RUN cd /root && \
    wget https://github.com/requests/requests/tarball/master && \
    tar -xvf master && \
    cd requests-* && \
    pip install .

ENV home /home/ctfs
WORKDIR $home