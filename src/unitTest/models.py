from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=30)
    editor = models.CharField(max_length=30)
    nb_players = models.IntegerField()

