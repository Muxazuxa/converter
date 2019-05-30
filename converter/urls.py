from django.urls import path
from .views import *

app_name = 'converter'

urlpatterns = [
    path('', converter, name='converter'),
    path('download/<str:name>', download, name='download')
]