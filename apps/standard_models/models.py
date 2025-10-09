from django.db import models
from apps.observations.models import Observation
from apps.constructions.models import Construction
from apps.referentials.models import Referential
from django.utils.translation import gettext_lazy as _


class StandardModel(models.Model):
    name = models.CharField(max_length=250, verbose_name=_("Standard name"))

    num_housing_units = models.IntegerField(default=0)
    num_adapted_units = models.IntegerField(default=0)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)

    referentials = models.ManyToManyField(Referential, related_name="standard_models")
    observations = models.ManyToManyField(Observation, related_name="standard_models")

    def __str__(self):
        return self.name

