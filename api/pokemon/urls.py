from django.contrib import admin
from django.urls import path, include
from .views import PokemonList, PokemonDetail, PokemonRestore, PokemonForeDelete

urlpatterns = [
    path('', PokemonList.as_view(), name='pokemon.list'),
    path('<int:pk>/', PokemonDetail.as_view(), name='pokemon.detail'),
    path('<int:pk>/restore/', PokemonRestore.as_view(), name='pokemon.restore'),
    path('<int:pk>/force/', PokemonForeDelete.as_view(), name='pokemon.force'),
]