from django.contrib import admin
from .models import Referential, ReferentialName

# Register your models here.
admin.site.register(ReferentialName)
admin.site.register(Referential)
