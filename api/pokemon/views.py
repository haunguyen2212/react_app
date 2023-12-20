from rest_framework import generics
from pokemon.models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.
class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
