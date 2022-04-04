from django import forms

from yt_app.models import Tournament, Place, Game, Team
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
