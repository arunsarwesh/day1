from django.db import models

class Books(models.Model):

    title = models.CharField(max_length = 80)
    summary = models.TextField(max_length=2000)
    pages = models.CharField(max_length=80)
    availability = models.IntegerField(default=0)
    author = models.CharField(max_length=80)
    author_id = models.IntegerField(default=0)
    
    
# Create your models here.
