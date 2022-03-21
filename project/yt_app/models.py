from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=True)


class Match(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Games(models.Model):  
    G_TYPES = (
        (1, "RTS"),
        (2, "FPS"),
        (3, "MOBA")
    )
    game_type = models.IntegerField(choices=G_TYPES)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    tournaments = models.ManyToManyField(Tournament)


class Scores(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    name1 = models.CharField(max_length=30)


class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    tournaments = models.ManyToManyField(Tournament)
