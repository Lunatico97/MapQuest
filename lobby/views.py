from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say(request):
	return HttpResponse('<h1> Hello World ! </h1>') ;