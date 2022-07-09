from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "recipes/home.html", context={'name': 'Jonathan Rodrigo'})


def contato(request):
    return HttpResponse("recipes/contato.html")


def sobre(request):
    return HttpResponse("Sobre")


# Create your views here.
