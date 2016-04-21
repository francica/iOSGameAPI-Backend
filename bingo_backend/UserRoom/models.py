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

    def to_dict(self):
        ret = {}
        ret['user_id'] = self.user_id
        ret['name'] = self.name
        ret['score'] = self.score
        return ret

class Room(models.Model):
    room_id = models.AutoField(primary_key = True)
    owner_id = models.IntegerField()
    users = models.TextField()
    board_id = models.IntegerField(default = 0)
    name = models.CharField(max_length = 100)
    game_status = models.BooleanField(default = False)
    drawer = models.IntegerField(default = 0)
    scores = models.TextField(default = '')

    def to_dict(self):
        ret = {}
        ret['room_id'] = self.room_id
        ret['owner_id'] = self.owner_id
        ret['name'] = self.name
        ret['drawer'] = self.drawer
        return ret
