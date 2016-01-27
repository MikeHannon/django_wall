from __future__ import unicode_literals
# uses the prebuilt user from django autherization
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Message(models.Model):
    # sets datetime to the current time
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now everytime record updated
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_creator = models.ForeignKey(User)
