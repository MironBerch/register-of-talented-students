FROM python:3.10


WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    net-tools

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt