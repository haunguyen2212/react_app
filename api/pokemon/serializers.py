from rest_framework import serializers
from pokemon.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'no', 'name', 'primary_type', 'secondary_type', 'weight', 'height', 'description')
        
    def validate(self, data):
        if 'primary_type' not in data or data['primary_type'] is None:
            raise serializers.ValidationError({'primary_type':'This field is required.'})
        return data