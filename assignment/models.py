from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    sroll = models.IntegerField()
    sname = models.CharField( max_length=200)
    sfname = models.CharField( max_length=200)
    sage = models.IntegerField()
