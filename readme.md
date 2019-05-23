
### Youtube Video Converter

## Description

Converts youtube video to mp3 format.

## Installation

> 1.Install Python 3.6 and newer

> 2.Clone repository: `git clone https://github.com/Muxazuxa/video-converter.git`

> 3.`cd` into `videoconverter`

> 4.Install virtualenv

>5.Create new environment `virtualenv env`

>6.Activate env:`source env/bin/activate`

>7.Install required packages: `pip install -r requirements.txt`

>8.Create .env file and set your variables

>9.Make migrations to database: `python manage.py makemigrations` and `python manage.py migrate`

>10.Run `python manage.py runserver`

>11.Open second terminal and also run `celery worker -A video_converter --loglevel=debug --concurrency=4`
