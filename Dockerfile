FROM centos:centos7

RUN yum update -y

RUN yum install -y file

# Uses to get information of Images and converts to between image types.
RUN yum install -y ImageMagick-devel

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u

ENV home /home/ctfs
WORKDIR $home