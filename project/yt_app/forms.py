from django import forms
from yt_app.models import Tournament, Place, Game, Team, Match
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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

    def clean(self):
        cleaned_data = super().clean()

        team1 = cleaned_data.get('team1')
        team2 = cleaned_data.get('team2') 

        if team1 == team2:
            raise forms.ValidationError('Teams have to be different')


class AddDuelForm(forms.Form):
    match_field = forms.ModelChoiceField(queryset=Match.objects.all(), label='Match')




class UpdateTeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    tournaments_ch= forms.ModelMultipleChoiceField(queryset=Tournament.objects.all(), label='Change tournaments')
    players_ch = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label='Change players')

