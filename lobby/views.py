from django.shortcuts import render ;
from django.http import HttpResponse ;
from .models import Lobby ;

# Create your views here.
def lobby(request):
	lobbies = Lobby.objects.all() ;
	context = {"lobbies": lobbies} ;
	return HttpResponse(render(request, 'lobby.html', context)) ;

def lobby_view(request, id):
	if id:
		lobby = Lobby.objects.get(pk=id) ;
	else:
		lobby = '' ;
	context = {"lobby": lobby} ;
	return HttpResponse(render(request, 'lobby_view.html', context)) ;
