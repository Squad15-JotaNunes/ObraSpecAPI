from django.db import models


# Create your models here.
class Referential(models.Model):
    name = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)
    comment = models.TextField(max_length=500)
    # Falta ambientes
