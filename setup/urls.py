from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_patterns = [
    path("observations/", include("apps.observations.urls")),
    path("materials/", include("apps.materials.urls")),
    path("elements/", include("apps.elements.urls")),
    path("areas/", include("apps.areas.urls")),
    path("referentials/", include("apps.referentials.urls")),
    path("standard-models/", include("apps.standard_models.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("authentication/", include("apps.authentication.urls")),
    path("constructions/", include("apps.constructions.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="API JotaNunes",
        default_version="v1",
        description="Descrição da API",
        contact=openapi.Contact(email="jotanunes@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
    patterns=api_patterns,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    *api_patterns,
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
