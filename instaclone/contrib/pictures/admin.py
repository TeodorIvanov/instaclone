import re

from django.contrib import admin
from django.forms import ModelForm

from . import models
from instaclone.contrib.tags.models import Tag
from instaclone.contrib.tags.utils import get_hashtags_from_description


@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):

    def save_related(self, request, form, formsets, change):
        """
        Custom save_related method to override default behavior when saving m2m relationships
        through the django admin.
        """
        super(PictureAdmin, self).save_related(request, form, formsets, change)
        pic_tags = get_hashtags_from_description(form.instance)
        form.instance.tags.add(*pic_tags)
