from django.contrib import admin
from .models import Tournament, Player, Team
from matches.models import Match
# Register your models here.

admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
