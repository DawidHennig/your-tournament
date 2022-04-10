from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
from yt_app.forms import AddTournamentForm, AddTeamForm, AddMatchForm, AddDuelForm
from yt_app.models import (
        Place, 
        Game, 
        Tournament,
        Team,
        Match,
        Duel,
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

@pytest.mark.django_db
def test_duel_model(duel):
    assert len(Duel.objects.all()) == 1
    assert Duel.objects.get(pk=1) == duel

@pytest.mark.django_db
@pytest.mark.parametrize("url", (
    'index',
    'list_tournaments',
    'login',
    'register',
    ))
def test_urls_nologin_access(url):
    c = Client() 
    resp = c.get(reverse(url))
    assert resp.status_code == 200

@pytest.mark.django_db
@pytest.mark.parametrize("url", (
    'add_tournament',
    'add_team',
    'add_match',
    'add_duel',
    'view_teams',
    'update_team',
    'view_duel'
    ))
def test_urls_nologin_access_required(url):
    c = Client() 
    resp = c.get(reverse(url))
    assert resp.status_code == 302 

@pytest.mark.django_db
@pytest.mark.parametrize("url", (
    'index',
    'list_tournaments',
    'login',
    'register',
    'add_tournament',
    'add_team',
    'add_match',
    'add_duel',
    'view_teams',
    'update_team',
    'view_duel'
    ))
def test_urls_login(user, url):
    c = Client() 
    c.force_login(user)
    resp = c.get(reverse(url))
    assert resp.status_code == 200 

@pytest.mark.django_db
@pytest.mark.parametrize("url", (
    'index',
    'add_place',
    'add_game',
    'list_tournaments',
    'login',
    'register',
    'add_tournament',
    'add_team',
    'add_match',
    'add_duel',
    'view_teams',
    'update_team',
    'view_duel'
    ))
def test_urls_superlogin(superuser, url):
    c = Client() 
    c.force_login(superuser)
    resp = c.get(reverse(url))
    assert resp.status_code == 200 

@pytest.mark.django_db
@pytest.mark.parametrize("url", (
    'add_game',
    'add_place',
    ))
def test_urls_login_superuser_access(user, url):
    c = Client() 
    c.force_login(user)
    resp = c.get(reverse(url))
    assert resp.status_code == 403 


@pytest.mark.django_db
@pytest.mark.parametrize("url, form", (
    ('add_tournament', AddTournamentForm),
    ('add_team', AddTeamForm),
    ('add_match', AddMatchForm),
    ('add_duel', AddDuelForm),
    ))
def test_login_form_get(user, url, form):
    c = Client() 
    c.force_login(user)
    resp = c.get(reverse(url))
    assert resp.status_code == 200 
    assert isinstance(resp.context['form'], form)
