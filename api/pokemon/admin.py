from django.contrib import admin
from . import models

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return models.Pokemon.all_objects.all()

admin.site.register(models.Type, MyModelAdmin)
admin.site.register(models.Pokemon, MyModelAdmin)