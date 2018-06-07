FROM centos:centos7

RUN yum update -y && yum install -y wget make vim

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u python36u-pip java-1.8.0-openjdk-devel && \
    pip3.6 install --upgrade pip

RUN yum install -y centos-release-scl && \
    yum install -y rh-ruby23

###################################################################################################
# Forensics
RUN yum install -y e4fsprogs \
    file \
    ImageMagick-devel \
    perl-devel \
    unzip \
    wireshark \
    zip

RUN source scl_source enable rh-ruby23 && \
    gem install zsteg

RUN cd /root && \
    wget https://www.sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-10.99.tar.gz && \
    tar -xvf Image-ExifTool-10.99.tar.gz && \
    cd Image-ExifTool-10.99 && \
    perl Makefile.PL && \
    make install

RUN cd /root && \
    wget https://github.com/requests/requests/tarball/master && \
    tar -xvf master && \
    cd requests-* && \
    pip install .

ENTRYPOINT ["/usr/bin/scl", "enable", "rh-ruby23", "--"]
CMD ["/usr/bin/scl", "enable", "rh-ruby23", "--", "/bin/bash"]
