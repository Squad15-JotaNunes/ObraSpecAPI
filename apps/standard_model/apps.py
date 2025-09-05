from django.apps import AppConfig


class StandardModelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.standard_model"
