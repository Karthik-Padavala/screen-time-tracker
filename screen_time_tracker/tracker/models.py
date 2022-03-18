from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=20)
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()
    time = models.IntegerField()