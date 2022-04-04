from django.shortcuts import render, redirect
from django.views import View 

from yt_app.forms import AddTournamentForm, AddPlaceForm, AddGameForm, AddTeamForm, AddMatchForm
from yt_app.models import Tournament, Place, Game, Team, Match
# Create your views here.



class Index(View):

    def get(self, request):
        return render(request, "index.html",)


class AddTournamentView(View):
    def get(self, request):
        form = AddTournamentForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddTournamentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            place = form.cleaned_data["place"]
            game = form.cleaned_data["game"]
            t_obj = Tournament.objects.create(name=name, description=description)
            t_obj.place.add(place)
            t_obj.game.add(game)


            return redirect("index")
        return redirect("add_place")


class AddPlaceView(View):
    def get(self, request):
        form = AddPlaceForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddPlaceForm(request.POST)
        if form.is_valid():
            Place.objects.create(**form.cleaned_data)
            return redirect("add_place")

        return redirect("index")


class AddGameView(View):
    def get(self, request):
        form = AddGameForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddGameForm(request.POST)
        if form.is_valid():
            Game.objects.create(**form.cleaned_data)
            return redirect("index")

        return redirect("add_game")


class AddTeamView(View):
    def get(self, request):
        form = AddTeamForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddTeamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            tournaments = form.cleaned_data["tournaments"]
            players = form.cleaned_data["players"]
            t_obj = Team.objects.create(name=name)
            t_obj.tournaments.add(tournaments)
            t_obj.players.set(players)

            return redirect("index")
        return redirect("add_place")


class AddMatchView(View):
    def get(self, request):
        form = AddMatchForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddMatchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            team1 = form.cleaned_data["team1"]
            team2 = form.cleaned_data["team2"]
            m_obj = Match.objects.create(name=name, team1=team1, team2=team2)

            return redirect("index")
        return redirect("add_place")
