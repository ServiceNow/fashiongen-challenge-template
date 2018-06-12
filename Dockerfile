FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
        apt-get -y install \
        wget \
        curl \
        libcurl3 \
        libcurl4-openssl-dev \
        libssl-dev \
        gfortran \
        build-essential \
        make \
        gcc \
        build-essential \
        git-core \
        vim-tiny \
        nano \
        libffi-dev \
        python-pip \
        software-properties-common

RUN add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get -y install \
        python2.7 \
        python3.5 \
        python3.6 \
        python2.7-dev \
        python3.5-dev \
        python3.6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN add-apt-repository universe && \
        apt-get update --fix-missing && \
        apt-get -y install \
        libenchant1c2a \
        libhdf5-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install -U pip

RUN apt-get update --fix-missing && apt-get install -y libopenblas-dev \
    libblas-dev liblapack-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /temp_pip && \
    cd /temp_pip && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python2.7 get-pip.py && \
    python3.5 get-pip.py && \
    python3.6 get-pip.py

ADD ./requirements.txt /tmp/requirements.txt
RUN pip2.7 install --no-cache-dir -r /tmp/requirements.txt && \
    pip3.5 install --no-cache-dir -r /tmp/requirements.txt && \
    pip3.6 install --no-cache-dir -r /tmp/requirements.txt

ENV LANG C.UTF-8

WORKDIR /srv/app

COPY . /srv/app

CMD python run.py
