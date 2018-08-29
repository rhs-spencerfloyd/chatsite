from django.db import models

# Create your models here.
class Message(models.Model):
    message_text = models.TextField()
    ip = models.TextField()

class IPName(models.Model):
    ip = models.TextField()
    name = models.TextField()

class GetRequest(models.Model):
    ip = models.TextField()
    datetime = models.DateTimeField('datetime')