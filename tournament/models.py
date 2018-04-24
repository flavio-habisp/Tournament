from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.conf import settings

import uuid

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, help_text='Account number',blank=True, null=True)
    email = models.EmailField()

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.name, self.email)


class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, help_text='Player or Team', blank=True, null=True)
    team_ads = models.CharField(max_length=100,blank=True, null=True, help_text='The advertisement of the Team')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        if self.players.count() > 1:
            return '{}'.format(" - ".join(str(player.name) for player in self.players.all()))
        else:
            return '{}'.format(self.name)


class Tournament(models.Model):
    SPORT_TYPE = (
        ('pickleball', 'Pickleball'),
        ('squash', 'Squash '),
        ('tennis', 'Tennis'),
        ('table_tennis', 'Table Tennis'),
    )
    name = models.CharField(max_length=100, help_text='The public name of the tournament')
    slug = models.SlugField(max_length=100,blank=True, null=True)
    sport = models.CharField(max_length=200, choices=SPORT_TYPE)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    players = models.ManyToManyField(Team, help_text='Player or Team', blank=True)
    tournament_ads = models.CharField(max_length=100,blank=True, null=True, help_text='The advertisement of the tournament')

    def save(self, *args, **kwargs):
        """
        Make a slug from Tournament.name
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

