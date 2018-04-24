from django import forms
from tournament.models import Team, Player, Tournament

class TournamentForm(forms.ModelForm):

    class Meta:
        model = Tournament
        fields = ('name', 'sport','slug', 'tournament_ads' )