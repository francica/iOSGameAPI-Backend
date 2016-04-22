from django.db import models

# Create your models here.
class Word(models.Model):
    score=models.IntegerField(default = 0)
    text=models.CharField(max_length=100)
    word_id=models.AutoField(primary_key=True)
