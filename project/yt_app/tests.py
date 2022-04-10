from django.test import TestCase

# Create your tests here.
from yt_app.models import (
        Place, 
        Game, 
        Tournament,
        Team,
        Match,
        )
import pytest

@pytest.mark.django_db
def test_place_model(place):
    assert len(Place.objects.all()) == 1
    assert Place.objects.get(name="Hamburg") == place

@pytest.mark.django_db
def test_game_model(game):
    assert len(Game.objects.all()) == 1
    assert Game.objects.get(name="Dota 2") == game 

@pytest.mark.django_db
def test_tournament_model(tournament):
    assert len(Tournament.objects.all()) == 1
    assert Tournament.objects.get(name="Els One - Dota 2") == tournament 

@pytest.mark.django_db
def test_team_model(team):
    assert len(Team.objects.all()) == 1
    assert Team.objects.get(name="Test team") == team 

@pytest.mark.django_db
def test_match_model(match_model):
    assert len(Match.objects.all()) == 1
    assert Match.objects.get(name="Test match") == match_model 
