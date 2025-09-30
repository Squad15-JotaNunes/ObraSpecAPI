from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.elements.models import Element


# Nome Ambiente
class AreaName(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)

    def __str__(self):
        return self.name


# SetAreaElements
class Area(models.Model):
    area_name = models.ForeignKey(
        AreaName, on_delete=models.CASCADE, related_name="areas"
    )
    elements = models.ManyToManyField(Element, related_name="areas")

    def __str__(self):
        elements_list = ", ".join([str(e) for e in self.elements.all()])
        return f"Area: {self.area_name.name} - {elements_list if elements_list else 'None'}"
