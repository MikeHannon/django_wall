from __future__ import unicode_literals
# uses the prebuilt user from django autherization
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Comment(models.Model):
    # sets datetime to the current time
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now everytime record updated
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    comment_creator = models.ForeignKey(User)
