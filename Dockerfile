FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /conv

WORKDIR /conv

ADD . /conv/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system
RUN apt-get update && apt-get install -y ffmpeg