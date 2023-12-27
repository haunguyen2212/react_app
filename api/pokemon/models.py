from django.db import models
from django.utils import timezone

# Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
    
class InActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=False)
    
class Type(models.Model):
    name = models.CharField(max_length=30)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ActiveManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=100)
    primary_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='primary_type')
    secondary_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name='secondary_type')
    height = models.FloatField()
    weight = models.FloatField()
    description = models.CharField(max_length=3000, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ActiveManager()
    all_objects = models.Manager()
    deleted_objects = InActiveManager()
    
    class Meta:
        ordering = ('no',)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()
        
    def force_delete(self):
        return super().delete()
