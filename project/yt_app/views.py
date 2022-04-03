from django.shortcuts import render, redirect
from django.views import View 

from yt_app.forms import AddTournamentForm, AddPlaceForm, AddGameForm
from yt_app.models import Tournament, Place, Game
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
            test1 = Tournament.objects.create(name=name, description=description)
            test1.place.add(place)
            test1.game.add(game)


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
