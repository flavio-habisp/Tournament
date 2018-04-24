from django.shortcuts import render, get_object_or_404, redirect
#from tournament.models import Team, Player, Tournament
from django.views.generic import DetailView
from .models import Tournament, Player, Team, Match


def tourney_list(request):

    tourneys = Tournament.objects.all()
    return render(request, 'matches/tournament.html', {'tourneys': tourneys})
