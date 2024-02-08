from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobbies'),
    path('lobby/<int:id>/', views.lobby_view, name='lobby-view'),
]
