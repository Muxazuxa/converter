from django.contrib import admin
from .models import Data

# Register your models here.


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('url', 'email', 'created')
    list_filter = ('created', )