from django.conf.urls import url
from django.contrib import admin
from .views import news_feed, user_profile, toggle_like, toggle_follow

urlpatterns = [
    url(r'^$', news_feed, name='news_feed'),
    url(r'(?P<username>\w+)/$', user_profile, name='user_profile'),
    url(r'toggle-like', toggle_like, name='toggle_like'),
    url(r'toggle-follow', toggle_follow, name='toggle_follow')
]
