from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.utils.translation import ugettext as _
from .managers import UserManager


class BaseUser(models.Model):
    user = models.OneToOneField(DjangoUser, related_name='insta_user')

    class Meta:
        abstract = True


class User(BaseUser):
    first_name = models.CharField(_('First name'), max_length=255, default='')
    last_name = models.CharField(_('Last name'), max_length=255, default='')
    profile_picture = models.FileField()
    description = models.CharField(_('Profile description'), max_length=500, default='')
    is_public = models.BooleanField(_('Profile is public'), default=True)
    time_created = models.DateTimeField(_('Time created'), auto_now=False, auto_now_add=True)
    time_updated = models.DateTimeField(_('Last updated'), auto_now=True, auto_now_add=False)
    last_ip = models.GenericIPAddressField(_('Last user IP'), blank=True, null=True)
    followed_users = models.ManyToManyField("User", verbose_name=_('Followed users'),
                                            related_name='followers', blank=True, symmetrical=False)
    blocked_users = models.ManyToManyField("User", verbose_name=_('Blocked users'),
                                           related_name='blocked_by_users', blank=True, symmetrical=False)

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return 'User: {}'.format(self.user.username)


class Search(models.Model):
    query = models.CharField(_('Search query'), max_length=1000, default='')
    user = models.ForeignKey(User, verbose_name=_('User'))
    time_created = models.DateTimeField(_('Time created'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('Search')
        verbose_name_plural = _('Searches')
        index_together = ['user', 'query']
        order_with_respect_to = 'user'

    def __str__(self):
        return 'Search {}: {}'.format(self.user.user.username, self.query)
