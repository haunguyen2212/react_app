from rest_framework import serializers
from pokemon.models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Type
        fields = ('id', 'name')

class PokemonSerializer(serializers.ModelSerializer):
    primary_type = TypeSerializer(read_only=True)
    secondary_type = TypeSerializer(read_only=True)
    primary_type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), 
        source='primary_type', 
        write_only=True
    )
    secondary_type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), 
        source='secondary_type', 
        write_only=True,
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = Pokemon
        fields = ('no', 'name', 'primary_type', 'secondary_type', 'weight', 'height', 'description', 'primary_type_id', 'secondary_type_id')