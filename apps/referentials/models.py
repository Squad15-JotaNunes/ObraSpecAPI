from django.db import models
from apps.areas.models import Area


class ReferentialName(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Referential(models.Model):
    referential_name = models.ForeignKey(
        ReferentialName, on_delete=models.CASCADE, related_name="referentials"
    )
    areas = models.ManyToManyField(Area, related_name="referentials")

    is_approved = models.BooleanField(default=False)
    comment = models.TextField(max_length=500, blank=True)

    def __str__(self):
        areas_list = ", ".join([str(a) for a in self.areas.all()])
        return f"Referential: {self.referential_name.name} - [{areas_list if areas_list else 'None'}]"
