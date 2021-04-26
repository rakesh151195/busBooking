from django.db import models

# Create your models here.

class DataStore(models.Model):
    source = models.TextField(default='')
    dest = models.TextField(default='')
    busNo = models.TextField(default='')
