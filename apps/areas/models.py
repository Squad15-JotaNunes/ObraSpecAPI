from django.db import models
from django.utils.translation import ugettext_lazy as _


# Ambiente
class Area(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    # adicionar conjunto de elementos.


class SetAreaElements(models.Model):
    pass
