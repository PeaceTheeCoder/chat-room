from django.db import models

# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True,blank=True)