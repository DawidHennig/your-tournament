from django.shortcuts import render, redirect
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from mixins import SuperuserRequiredMixin
from django.views.generic import ListView, UpdateView

from yt_app.forms import AddTournamentForm, AddPlaceForm, AddGameForm, AddTeamForm, AddMatchForm, AddDuelForm, UpdateTeamForm
from yt_app.models import Tournament, Place, Game, Team, Match, Duel
# Create your views here.



class Index(View):

    def get(self, request):
        return render(request, "index.html",)


class AddTournamentView(LoginRequiredMixin, View):
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
        return redirect("add_tournament")


class AddPlaceView(SuperuserRequiredMixin, View):
    def get(self, request):
        form = AddPlaceForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddPlaceForm(request.POST)
        if form.is_valid():
            Place.objects.create(**form.cleaned_data)
            return redirect("add_place")

        return redirect("index")


class AddGameView(SuperuserRequiredMixin, View):
    def get(self, request):
        form = AddGameForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddGameForm(request.POST)
        if form.is_valid():
            Game.objects.create(**form.cleaned_data)
            return redirect("index")

        return redirect("add_game")


class AddTeamView(LoginRequiredMixin, View):
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
        return redirect("add_team")


class AddMatchView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddMatchForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddMatchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            team1 = form.cleaned_data["team1"]
            team2 = form.cleaned_data["team2"]
            tournament = form.cleaned_data["tournament"]
            Match.objects.create(name=name, team1=team1, team2=team2, tournament=tournament)

            return redirect("index")
        return redirect("add_match")


class AddDuelView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddDuelForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        form = AddDuelForm(request.POST)
        if form.is_valid():
            match_field = form.cleaned_data["match_field"]
            name = f'{match_field.team1} vs {match_field.team2}'
            Duel.objects.create(name=name, match_field=match_field)

            return redirect("index")
        return redirect("add_duel")


class ListTournaments(ListView):
    model = Tournament
    template_name = "tournament_list.html"


class ViewTeams(LoginRequiredMixin, ListView):
    model = Team 
    template_name = "obj_list_url.html"


class TeamDetail(View):

    def get(self, request, id):
        team = Team.objects.get(id=id)
        tournaments = team.tournaments.all()
        players = team.players.all()

        return render(request, 'team.html', {'team': team, 'tournaments': tournaments, 'players': players})


class UpdateTeam(LoginRequiredMixin, View):

    def get(self, request):
        form = UpdateTeamForm()
        return render(request, "form.html", {'form': form})


    def post(self, request):
        form = UpdateTeamForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data["team"]
            tournaments_ch  = form.cleaned_data["tournaments_ch"]
            players_ch= form.cleaned_data["players_ch"]
            team.tournaments.clear()
            team.tournaments.set(tournaments_ch)
            team.players.clear()
            team.players.set(players_ch)

            return redirect("index")
        return redirect("update_team")


class ViewDuel(LoginRequiredMixin, View):
    def get(self, request):
        matches = Match.objects.all()

        return render(request, 'duel_list.html', {'matches': matches})


class UpdateDuel(LoginRequiredMixin, UpdateView):
    model = Duel
    template_name = 'update_duel.html' 
    success_url = '/view_duel'
    fields = ['winner']
