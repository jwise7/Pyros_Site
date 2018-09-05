from django.db import models

# Create your models here.

class STournament(models.Model):
    tournament_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class STournament_Participant(models.Model):
    tournament = models.ForeignKey('STournament')
    player_name = models.CharField(max_length=200)

class STournament_Match(models.Model):
    match_num = models.IntegerField(default=1)
    tournament = models.ForeignKey('STournament')
    participant1 = models.ForeignKey('STournament_Participant')
    participant2 = models.ForeignKey('STournament_Participant')
    winner = models.ForeignKey('STournament_Participant')

#NOTE: match_num combined with the total number of entrants should give all the information needed to create a single elimination bracket. Idea copied from: https://dba.stackexchange.com/questions/7887/best-way-to-design-tournament-database

#EXAMPLE:
#    A
# match 1 -----+
#    B         A
#           match 5 -----+
#    C         C         |
# match 2 -----+         |
#    D                   A
#                     match 7
#    E                   F
# match 3 -----+         |
#    F         F         |
#           match 6 -----+
#    G         G
# match 4 -----+
#    H