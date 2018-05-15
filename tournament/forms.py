from django import forms
from tournament.models import Team, Player, Tournament


class TournamentFormObj(forms.ModelForm):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'sport','slug', 'start_datetime', 'end_datetime', 'tournament_ads', )
