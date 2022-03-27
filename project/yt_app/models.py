from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=True)


class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    tournaments = models.ManyToManyField(Tournament)


class Games(models.Model):  
    G_TYPES = (
        (1, "RTS"),
        (2, "FPS"),
        (3, "MOBA"),
        (4, "Other"),
    )
    game_type = models.IntegerField(choices=G_TYPES, default=4)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    tournaments = models.ManyToManyField(Tournament)


class Match(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Duel(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
