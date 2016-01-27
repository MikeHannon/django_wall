# python 2-3 conversion: b'<-- python2 u'<-- python3
from __future__ import unicode_literals
# uses the prebuilt user from django autherization
from django.contrib.auth.models import User
from django.db import models
import datetime
#import message and comments
from django.apps import apps

Comment = apps.get_app_config('comments').models['comment']
Message = apps.get_app_config('posts').models['message']

class Wall(models.Model):
    user = models.OneToOneField(User)


class Wall_User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #USER has email, password (hashed)(r), username(r), first name, last name
    DOB = models.DateField()


class Wall_Comment(Comment):
    message_id = models.ForeignKey(Message)

class Wall_Message(Message):
    wall = models.ForeignKey(Wall)
