FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /converter
WORKDIR /converter
ADD . /converter/
RUN pip install pipenv
RUN pipenv install --system
RUN apt-get update && apt-get install -y ffmpeg