from django.shortcuts import render
from django.views import View 

from yt_app.forms import AddTournamentModelForm
# Create your views here.



class Index(View):

    def get(self, request):
        return render(request, "index.html",)


class AddTournamentView(View):
    def get(self, request):
        form = AddTournamentModelForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        pass

