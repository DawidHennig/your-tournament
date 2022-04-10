from yt_app.models import (
        Tournament, 
        Match, 
        Duel, 
        Team, 
        Place, 
        Game, 
        Team,
        User,
        Match,
        Duel,
        )
import pytest


@pytest.fixture
def place():
    return Place.objects.create(
                            name="Hamburg",
                            description="nice place",
                            address="hamburg 1"
                            )

@pytest.fixture
def game():
    return Game.objects.create(
                        game_type=4,
                        name="Dota 2",
                        description="Nice moba game"
                        )


@pytest.fixture
def tournament():
    Tournament.objects.create(
                    name="Els One - Dota 2",
                    description="Big dota 2 tournament price 200$ for winners!",
                    )
    Place.objects.create(
                    name="Hamburg",
                    description="nice place",
                    address="hamburg 1"
                    )
    Game.objects.create(
                    game_type=4,
                    name="Dota 2",
                    description="Nice moba game"
                    )

    tournament = Tournament.objects.get(pk=1)
    place = Place.objects.get(pk=1) 
    game = Game.objects.get(pk=1) 
    tournament.place.add(place)
    tournament.game.add(game)
    return tournament

@pytest.fixture
def team():
    team = Team.objects.create(name="Test team")
    user = User.objects.create_user(username="test user", password="123")
    team.players.add(user)
    return team

@pytest.fixture
def match_model():
    team = Team.objects.create()
    tournament = Tournament.objects.create()
    return Match.objects.create(name="Test match", team1=team, team2=team, tournament=tournament)

@pytest.fixture
def duel():
    team = Team.objects.create()
    tournament = Tournament.objects.create()
    match_model = Match.objects.create(name="Test match", team1=team, team2=team, tournament=tournament)
    match_m = Match.objects.get(name="Test match")
    duel = Duel.objects.create(match_field=match_m)
    return duel 

@pytest.fixture
def user():
    return User.objects.create_user(username="test", password="test")

@pytest.fixture
def superuser():
    return User.objects.create_superuser(username="supertest", password="supertest")
