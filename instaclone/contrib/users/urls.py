from django.conf.urls import url
from django.contrib import admin
from .views import news_feed

urlpatterns = [
    url(r'^', news_feed, name='news_feed'),
]
