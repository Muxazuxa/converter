import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_converter.settings')
app = Celery('video_converter')
app.config_from_object('django.conf.settings')
app.autodiscover_tasks()