import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_converter.settings')
app = Celery('video_converter', broker='redis://localhost:6379')
app.config_from_object('django.conf.settings')
app.autodiscover_tasks()