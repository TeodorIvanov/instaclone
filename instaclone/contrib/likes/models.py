from django.db import models
from django.utils.translation import ugettext as _

from instaclone.contrib.pictures.models import Picture
from instaclone.contrib.users.models import User


class Like(models.Model):
    user = models.OneToOneField(User, verbose_name=_('Liked by user'))
    picture = models.OneToOneField(Picture, verbose_name=_('Liked picture'))
    time_updated = models.DateTimeField(_('Last updated'), auto_now=True, auto_now_add=False)
