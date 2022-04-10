"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yt_app.views import (
        Index, 
        AddTournamentView,
        AddPlaceView, 
        AddGameView, 
        AddTeamView, 
        AddMatchView, 
        AddDuelView, 
        ListTournaments, 
        ViewTeams, 
        UpdateTeam, 
        TeamDetail,
        ViewDuel,
        UpdateDuel,
        )
from acc.views import LogInView, LogOutView, RegisterView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('add_tournament', AddTournamentView.as_view(), name='add_tournament'),
    path('add_place', AddPlaceView.as_view(), name='add_place'),
    path('add_game', AddGameView.as_view(), name='add_game'),
    path('add_team', AddTeamView.as_view(), name='add_team'),
    path('add_match', AddMatchView.as_view(), name='add_match'),
    path('add_duel', AddDuelView.as_view(), name='add_duel'),
    path('list_tournaments', ListTournaments.as_view(), name='list_tournaments'),
    path('view_teams', ViewTeams.as_view(), name='view_teams'),
    path('update_team', UpdateTeam.as_view(), name='update_team'),
    path('detail_team/<int:id>/', TeamDetail.as_view(), name='detail_team'),
    path('view_duel', ViewDuel.as_view(), name='view_duel'),
    path('update_duel/<int:pk>/', UpdateDuel.as_view(), name='update_duel'),
    path('login', LogInView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
]
