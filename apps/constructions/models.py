from django.db import models
from apps.observations.models import Observation
from django.utils.translation import gettext_lazy as _


class Construction(models.Model):
    project_name = models.CharField(max_length=250, null=False)
    location = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    num_housing_units = models.IntegerField()
    num_adapted_units = models.IntegerField()
    land_area = models.DecimalField(max_digits=10, decimal_places=2)

    # observations = models.ManyToManyField(
    #     Observation, "Observacao"
    # )  # Verificar melhor related name para um field externo.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
