from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # Home
    path('contato/', contato),  # Contato
    path('sobre/', sobre)
]
