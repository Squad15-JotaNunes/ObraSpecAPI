from django.db import models

# Create your models here.

class Observation(models.Model):
    description = models.TextField(verbose_name="description", blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.description