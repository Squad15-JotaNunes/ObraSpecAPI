from django.db import models
from apps.observations.models import Observation
from django.core.validators import MinValueValidator
from apps.referentials.models import Referential

from django.utils.translation import gettext_lazy as _


class Construction(models.Model):
    project_name = models.CharField(
        max_length=250, null=False, verbose_name=_("Project name")
    )

    location = models.CharField(max_length=250, null=False, verbose_name=_("Location"))
    description = models.TextField(
        max_length=1000, null=False, verbose_name=_("Description")
    )

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
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Land area"),
    )

    referentials = models.ManyToManyField(
        Referential, verbose_name=_(""), related_name="constructions"
    )
    observations = models.ManyToManyField(
        Observation,
        verbose_name=_("Observations"),
        related_name="constructions",
    )

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))


    def __str__(self):
        return self.project_name
    

class ConstructionReferential(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    referential = models.ForeignKey(Referential, on_delete=models.CASCADE)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["construction", "referentials"],
                name="unique_construction_referential"
            )
        ]

    def __str__(self):
        return f"{self.construction.project_name} - {self.referential.name}"


class ConstructionObservation(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
  

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["construction", "observations"],
                name="unique_construction_observation"
            )
        ]

    def __str__(self):
        return f"{self.construction.project_name} - {self.observation}"
 