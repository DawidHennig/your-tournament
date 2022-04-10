from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Game(models.Model):  
    G_TYPES = (
        (1, "RTS"),
        (2, "FPS"),
        (3, "MOBA"),
        (4, "Other"),
    )
    game_type = models.IntegerField(choices=G_TYPES)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    place = models.ManyToManyField(Place)
    game = models.ManyToManyField(Game)

    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=30)
    tournaments = models.ManyToManyField(Tournament, null=True)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return f'/detail_team/{self.id}/'

class Match(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    team1 = models.ForeignKey(Team, related_name="team1", on_delete=models.CASCADE, default=None)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Duel(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    match_field = models.ForeignKey(Match, on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def get_teams(self):
        return [self.match_field.team1, self.match_field.team2]

    def __str__(self):
        return self.name

    def get_update_url(self):
        return f'/update_duel/{self.id}/'
