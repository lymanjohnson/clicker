from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from game.models import Game, Player
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

class WelcomeScreen(TemplateView):
    pass

class PlayerList(ListView):
    pass

class PlayerRegister(FormView):
    pass

class PlayerLogin(TemplateView):
    pass

class PlayerDetail(DetailView):
    pass

class PlayerGameList(ListView):
    pass

class GamePlay(TemplateView):
    pass
