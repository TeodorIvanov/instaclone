from django.db import models
from django.utils.translation import ugettext as _


class Tag(models.Model):
    title = models.CharField(_('Title'), max_length=255, default='')
