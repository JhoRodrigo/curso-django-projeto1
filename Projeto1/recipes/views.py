# https://fontawesome.com/search?m=free&s=solid%2Cregular%2Cbrands icons
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Jonathan', })
