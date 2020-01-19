from django.contrib import admin
from . import models


@admin.register(models.Review)
class RebiewAdmin(admin.ModelAdmin):
    """Rebiew Admin Definition """

    pass
