FROM python:3.8.3

RUN mkdir /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        libopencv-dev \ 
        build-essential \
        libssl-dev \
        libpq-dev \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        postgresql \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip 
RUN pip3 install psycopg2 pipenv

COPY ./Pipfile /app/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY ./ecommerce/ /app/
