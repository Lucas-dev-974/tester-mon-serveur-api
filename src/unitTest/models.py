from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=30)
    editor = models.CharField(max_length=30)
    nb_players = models.IntegerField(validators=[MinValueValidator(0)])

