from __future__ import unicode_literals

from django.db import models
# import json
#from rest_framework import serializers

# Create your models here.

class User(models.Model):
    #user_id = models.BigIntegerField()
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    score = models.IntegerField(default = 0)

class Room(models.Model):
    room_id = models.AutoField(primary_key = True)
    owner_id = models.IntegerField()
    users = models.TextField()
    board_id = models.IntegerField(default = 0)
    name = models.CharField(max_length = 100)
    game_status = models.BooleanField(default = False)
    drawer = models.IntegerField(default = 0)
    scores = models.TextField(default = '')
