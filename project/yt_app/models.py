from django.db import models
from django.contrib.auth.models import User

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


class Team(models.Model):
    name = models.CharField(max_length=30)
    tournaments = models.ManyToManyField(Tournament, default=None)
    user = models.ManyToManyField(User)


class Match(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    team1 = models.ForeignKey(Team, related_name="team1", on_delete=models.CASCADE, default=None)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)


class Duel(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    match_field = models.ForeignKey(Match, on_delete=models.CASCADE, default=None)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
