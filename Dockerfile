FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /converter
WORKDIR /converter
ADD . /converter/
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg