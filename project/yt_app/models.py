from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Games(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    tournaments = models.ManyToManyField(Tournament)


class Scores(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    tournaments = models.ManyToManyField(Tournament)
