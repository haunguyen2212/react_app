from django.contrib import admin
from django.urls import path, include
from .views import PokemonList, PokemonDetail

urlpatterns = [
    path('', PokemonList.as_view(), name='pokemon.list'),
    # path('<int:pk>/', PokemonDetail.as_view(), name='pokemon.detail')
]