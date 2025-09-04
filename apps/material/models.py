from django.db import models

# Create your models here.
class Material(models.Model):
    type_of_material = models.CharField(max_length=50, verbose_name="type_of_material", blank=False)
    brands = models.CharField(max_length=255, verbose_name="brands", blank=False)
    description = models.TextField(verbose_name="description", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type_of_material