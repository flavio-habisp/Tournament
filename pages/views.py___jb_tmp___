from django.views.generic import TemplateView, FormView
from django.shortcuts import render, get_object_or_404, redirect
from djangox.forms import TournamentForm
from tournament.models import Tournament
from django.contrib.auth import get_user_model


class HomePageView(FormView):
    form_class = TournamentForm
    template_name = 'pages/home.html'
    success_url = '.'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


def home(request):
    User = get_user_model()
    tourneys = Tournament.objects.all()
    tournament_form = TournamentForm
    return render(request, 'pages/home.html', {'tourneys': tourneys, 'tournament_form': tournament_form})

