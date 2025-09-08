from django.db import models
from apps.materials.models import Material


class ElementType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# SetElementTypeMaterials
class Element(models.Model):
    element_type = models.ForeignKey(
        ElementType, on_delete=models.CASCADE, related_name="elements"
    )
    materials = models.ManyToManyField(Material, related_name="elements")

    # Talvez adicionar Meta -> UniqueConstraint para evitar recorrências iguais de element_type e materials

    def __str__(self):
        return f"Element: {self.element_type.name} - {self.materials}"
