from rest_framework import generics, status
from rest_framework.response import Response
from pokemon.models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.
class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonRestore(generics.UpdateAPIView):
    queryset = Pokemon.deleted_objects.all()
    serializer_class = PokemonSerializer
    
    def update(self, request, *args, **kwargs):
        return Response({'message': 'PUT method is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = None
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class PokemonForeDelete(generics.DestroyAPIView):
    queryset = Pokemon.all_objects.all()
    serializer_class = PokemonSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.force_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)