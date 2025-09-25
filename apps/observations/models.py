from django.db import models
from django.utils.translation import gettext_lazy as _


# Observação
class Observation(models.Model):
    description = models.TextField(verbose_name=_("description"), blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
