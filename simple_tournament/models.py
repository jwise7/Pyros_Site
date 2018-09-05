from django.db import models

# Create your models here.

class STournament(models.Model):
    tournament_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Participant(models.Model):
    player_name = models.CharField(max_length=200)

class STournamentTree(models.Model):
    round = models.IntegerField(default=1)
    order = models.IntegerField(default=0)
    tournament = models.ForeignKey('STournament')
    participant1 = models.ForeignKey('Participant')
    participant2 = models.ForeignKey('Participant')
    winner = models.ForeignKey('Participant')