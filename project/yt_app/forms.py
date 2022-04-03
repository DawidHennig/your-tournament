from django import forms

from yt_app.models import Tournament, Place, Game 


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
