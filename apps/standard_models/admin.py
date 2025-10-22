from django.contrib import admin
from apps.standard_models.models import StandardModel


@admin.register(StandardModel)
class StandardModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
