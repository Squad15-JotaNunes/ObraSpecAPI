from django.db import models

<<<<<<< Updated upstream
from ..obra.models import Obra
# Create your models here.

=======
# Observação
>>>>>>> Stashed changes
class Observation(models.Model):
    description = models.TextField(verbose_name="description", blank=False)
    construction = models.ForeignKey(Obra, on_delete=models.DO_NOTHING, related_name="observations")

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
