from django.db import models


class UserManager(models.Manager):

    def get_news_feed_items_for_user(self, user):
        return self.get(user=user).followed_users.all().prefetch_related('pictures', 'pictures__tags', 'pictures__likes')

    def get_user_profile_items(self, user_id):
        return self.get(id=user_id).prefetch_related('followed_users', 'pictures', 'pictures__tags', 'pictures__likes' 'blocked_users')
