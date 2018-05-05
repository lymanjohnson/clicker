from django.urls import path
from game import views

app_name = "game"
urlpatterns = [
    path('', views.WelcomeScreen.as_view(), name='welcome-screen'),
    path('player/', views.PlayerList.as_view(), name='player-list'),
    path('player/register/', views.PlayerRegister.as_view(), name='player-register'),
    path('player/login/', views.PlayerLogin.as_view(), name='player-login'),
    path('player/<str:handle>/', views.PlayerDetail.as_view(), name='player-detail'),
    path('player/<str:handle>/game/', views.PlayerGameList.as_view(), name='player-game-list'),
    path('player/<str:handle>/game/<int:pk>/', views.GamePlay.as_view(), name='gameplay'),
]
