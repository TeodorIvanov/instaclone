from django.db import models
from django.utils.translation import ugettext as _

from instaclone.contrib.users.models import User
from instaclone.contrib.tags.models import Tag


class Picture(models.Model):
    owner = models.ForeignKey(User, verbose_name=_('Owner'), related_name='pictures')
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), related_name='pictures')
    picture = models.FileField()
    description = models.CharField(_('Profile description'), max_length=500, default='')
    latitude = models.FloatField()
    logitude = models.FloatField()
    time_created = models.DateTimeField(_('Time created'), auto_now=False, auto_now_add=True)
    time_updated = models.DateTimeField(_('Last updated'), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Pictures')
        order_with_respect_to = 'owner'
