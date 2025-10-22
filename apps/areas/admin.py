from django.contrib import admin
from .models import Area, AreaName


@admin.register(AreaName)
class AreaNameAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["id", "area_name"]
    list_filter = ["area_name"]
    filter_horizontal = ["elements"]
