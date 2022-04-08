from django import forms

from yt_app.models import Tournament, Place, Game, Team, Match
from django.contrib.auth.models import User


class AddTournamentForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    place = forms.ModelChoiceField(queryset=Place.objects.all())
    game = forms.ModelChoiceField(queryset=Game.objects.all())


class AddPlaceForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    address = forms.CharField()


class AddGameForm(forms.Form):
    game_type = forms.ChoiceField(choices=Game.G_TYPES) 
    name = forms.CharField()
    description = forms.CharField()


class AddTeamForm(forms.Form):
    name = forms.CharField()
    tournaments = forms.ModelChoiceField(queryset=Tournament.objects.all())
    players = forms.ModelMultipleChoiceField(queryset=User.objects.all())


class AddMatchForm(forms.Form):
    name = forms.CharField()
    team1 = forms.ModelChoiceField(queryset=Team.objects.all())
    team2 = forms.ModelChoiceField(queryset=Team.objects.all())
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())


class AddDuelForm(forms.Form):
    name = forms.CharField()
    match_field = forms.ModelChoiceField(queryset=Match.objects.all(), label='Match')


class UpdateTeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    tournaments_add = forms.ModelMultipleChoiceField(queryset=Tournament.objects.all(), label='Add tournaments')
    tournaments_romove = forms.ModelMultipleChoiceField(queryset=Tournament.objects.all(), label='Romove tournaments')
    players_add = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label='Add players')
    players_rm = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label='Remove players')
