from django.contrib import admin
from . import models


@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
