from django.db import models
from django.urls import reverse, reverse_lazy

class Player(models.Model):
    handle = models.CharField(max_length=30)
    email = models.EmailField()
    games = models.ManyToManyField('Game')

    def __str__(self):
        return self.handle

class Game(models.Model):
    score = models.IntegerField(default=0)
    owner = models.ForeignKey('Player', on_delete = models.CASCADE)

    def __str__(self):
        return "%s's Game #%s, %s points" % self.owner.handle, self.pk, self.score
