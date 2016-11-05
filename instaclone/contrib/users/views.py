from collections import OrderedDict
from itertools import chain

from django.shortcuts import render
from .models import User


# @login_required
def news_feed(request):
    user = request.user
    news_feed = User.objects.get_news_feed_items_for_user(user=user)
    pictures = {}
    for user in news_feed:
        for item in user.pictures.all():
            pictures[item] = user
    qs = OrderedDict(sorted(pictures.items(), key=lambda instance: instance[0].time_created, reverse=True))
    context = {
        'objects': qs,
    }
    return render(request, 'news_feed.html', context)
