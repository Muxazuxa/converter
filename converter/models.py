from django.db import models

# Create your models here.


class Data(models.Model):
    url = models.URLField(max_length=200)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email