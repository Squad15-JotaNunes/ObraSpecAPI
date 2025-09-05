from django.db import models
from apps.observations.models import Observation
from django.core.validators import MinValueValidator

from django.utils.translation import gettext_lazy as _


class Construction(models.Model):
    project_name = models.CharField(
        max_length=250, null=False, verbose_name=_("Project name")
    )

    location = models.CharField(max_length=250, null=False, verbose_name=_("Location"))
    description = models.TextField(null=False, verbose_name=_("Description"))
    
    num_housing_units = models.IntegerField(
        verbose_name=_("Number housing units"),
        default=0,
        validators=[MinValueValidator(0)],
    )
    
    num_adapted_units = models.IntegerField(
        verbose_name=_("Number adapted units"),
        default=0,
        validators=[MinValueValidator(0)],
    )

    land_area = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Land area")
    )

    observations = models.ManyToManyField(
        Observation,
        verbose_name=_("Observacao"),
        through="SetConstructionObservations",
        related_name="related_constructions",
    )  # Verificar melhor related name para um field externo.

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return self.project_name


class SetConstructionObservations(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)

    class Meta:
        db_table = "set_construction_observations"

    def __str__(self):
        return f"{self.construction.project_name} - {self.observation.description[:30]}"
