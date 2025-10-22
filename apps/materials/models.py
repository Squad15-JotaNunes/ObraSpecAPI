from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    name = models.CharField(_("Material Type Name"), max_length=50, unique=True)

    def __str__(self):
        return self.name


# SetBrandMaterialType
class Material(models.Model):
    description = models.TextField(verbose_name=_("description"), blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="materials")
    material_type = models.ForeignKey(
        MaterialType, on_delete=models.CASCADE, related_name="materials"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "material_type"], name="unique_brand_material_type"
            )
        ]

    def __str__(self):
        return f"{self.material_type.name} - {self.brand.name}"
