from django.contrib import admin
from . import models


@admin.register(models.Review)
class RebiewAdmin(admin.ModelAdmin):
    """Rebiew Admin Definition """

    list_display = ("__str__", "rating_average")
