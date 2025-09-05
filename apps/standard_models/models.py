from django.db import models
from apps.observations.models import Observation


# Create your models here.
class StandardModel(models.Model):
    description = models.TextField(null=False)
    num_housing_units = models.IntegerField()
    num_adapted_units = models.IntegerField()
    land_area = models.DecimalField(max_digits=10, decimal_places=2)

    observations = models.ManyToManyField(
        Observation, "Observacao"
    )  # Verificar melhor related name para um field externo.
