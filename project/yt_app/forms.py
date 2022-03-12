from django import forms

from yt_app.models import Tournament 


class AddTournamentModelForm(forms.ModelForm):

    class Meta:
        model = Tournament
        exclude = ['created']

