from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from tournament.models import Player, Tournament, Team
import uuid


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    player_1_init = models.ForeignKey(Team, blank=True, null=True,
                                      related_name='home_game_match',
                                      help_text='Set for first round matches', on_delete=models.DO_NOTHING)
    player_2_init = models.ForeignKey(Team, blank=True, null=True,
                                      related_name='away_game_match',
                                      help_text='Set for first round matches', on_delete=models.DO_NOTHING)
    previous_match_1 = models.ForeignKey('Match', blank=True, null=True,
                                         related_name='subsequent_match_1', on_delete=models.DO_NOTHING)
    previous_match_2 = models.ForeignKey('Match', blank=True, null=True,
                                         related_name='subsequent_match_2', on_delete=models.DO_NOTHING)
    player_1_score = models.PositiveIntegerField(blank=True, null=True)
    player_2_score = models.PositiveIntegerField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    round_index = models.PositiveIntegerField(blank=True, null=True,
        help_text='The order of this match in the round (used for positioning).'
    )
    place = models.CharField(max_length=100,blank=True, null=True, help_text='The advertisement of the tournament')

    class Meta:
        verbose_name_plural = 'matches'

    def __str__(self):
        return '{} ({}) - {} vs. {}'.format(self.tournament, self.id, self.player_1, self.player_2)

    @property
    def player_1(self):
        """
        Return player_1_init or the winner of previous_match_1
        """
        return self.player_1_init or self.previous_match_1.winner()

    @property
    def player_2(self):
        """
        Return player_2_init or the winner of previous_match_2
        """
        return self.player_2_init or self.previous_match_2.winner()

    def winner(self):
        """
        Return the player with the highest score for the match
        """
        if self.player_1_score is None or self.player_2_score is None:
            return

        if self.player_1_score > self.player_2_score:
            return self.player_1
        if self.player_2_score > self.player_1_score:
            return self.player_2

    def save(self, *args, **kwargs):
        """
        Confirm that either both player fields or both match fields are set
        """
        player_error = False

        if (self.player_1_init and not self.player_2_init) \
                or (self.player_2_init and not self.player_1_init):
            player_error = True

        if (self.previous_match_1 and not self.previous_match_2) \
                or (self.previous_match_2 and not self.previous_match_1):
            player_error = True

        if (not self.player_1_init and not self.player_2_init) \
                and (not self.previous_match_1 and not self.previous_match_2):
            player_error = True

        if (self.player_1_init or self.player_2_init) \
                and (self.previous_match_1 or self.previous_match_2):
            player_error = True

        if player_error:
            raise ValidationError('Either both player fields or both match fields must be set.')

        super().save(*args, **kwargs)
