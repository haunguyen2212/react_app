from django.contrib import admin
from . import models

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return models.Pokemon.all_objects.all()
    
class TypeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return models.Type.all_objects.all()

admin.site.register(models.Type, TypeAdmin)
admin.site.register(models.Pokemon, PokemonAdmin)