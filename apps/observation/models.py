from django.db import models

# Create your models here.

class Observation(models.Model):
    description = models.TextField(verbose_name="description", blank=False)

    def __str__(self):
        return self.description