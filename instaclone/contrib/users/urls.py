from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import news_feed, user_profile, toggle_like, toggle_follow, logout_view

urlpatterns = [
    url(r'^$', news_feed, name='news_feed'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^(?P<username>\w+)/$', user_profile, name='user_profile'),
    url(r'toggle-like', toggle_like, name='toggle_like'),
    url(r'toggle-follow', toggle_follow, name='toggle_follow'),
]
