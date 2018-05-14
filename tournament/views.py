from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import TournamentFormObj
from .models import Tournament, Team, Player


def aplly_tournament(request):

    #import pdb;
    #pdb.set_trace()
    return redirect('home')


def validate(request):

    #import pdb;
    #pdb.set_trace()

    u_name = request.POST.get('name', None)
    t_id = request.POST.get('id', None)
    u_email = request.POST.get('email', None)
    u_number = request.POST.get('number', None)

    data = {
        'is_taken': True
    }
    data['error_message'] = ''
    player = Player()
    team = Team()

    player_exists = Player.objects.filter(email=u_email).exists()
    if not player_exists:
        player.name = u_name
        player.email = u_email
        player.number = u_number
        player.save()
        data['error_message'] += 'A user ' + u_name + ' created successfully.'
        team.name = u_name
        team.save()
        team.players.add(player)
        team.save()
        data['error_message'] += ' A team for ' + u_name + ' created successfully.'
    else:
        player = Player.objects.get(email=u_email)
        team = Team.objects.get(players=player)

    tournament = Tournament.objects.get(id=t_id)
    tournament.players.add(team)
    tournament.save()
    data['error_message'] += 'A user ' + u_name + ' applied successfully.'


    return JsonResponse(data)


def tournament_form(request):

    return render(request, 'tournament/tournament.html')


def tournament_new(request):

    modelTournament = TournamentFormObj(request.POST)
    if modelTournament.is_valid():
        modelTournament.save()

    return redirect('home')


def tournament_del(request, pk):

    _tournament = Tournament.objects.get(id=pk)
    _tournament.delete()
    return redirect('home')


def tournament(request, pk):

    _tournament = Tournament.objects.get(id=pk)
    _players = Tournament.objects.get(id=pk).players.all()

    return render(request, 'tournament/tourney.html', {'tournament': _tournament, 'players':_players})

