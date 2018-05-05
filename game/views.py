from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from game.models import Game, Player
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

class WelcomeScreen(TemplateView):
    template_name='welcome.html'

class PlayerList(ListView):
    model = Player
    template_name='player_list.html'

class PlayerRegister(TemplateView):
    template_name='player_register.html'

class PlayerLogin(TemplateView):
    template_name='player_login.html'

class PlayerDetail(DetailView):
    model = Player
    template_name='player_detail.html'

class PlayerGameList(ListView):
    model = Player
    template_name='player_game_list.html'

class GamePlay(TemplateView):
    model = Game
    template_name='game_play.html'
