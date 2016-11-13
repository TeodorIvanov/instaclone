from collections import OrderedDict
from itertools import chain

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from registration.backends.simple.views import RegistrationView

from .models import User
from instaclone.contrib.pictures.models import Picture
from instaclone.contrib.likes.models import Like


@login_required(login_url='/login/')
def news_feed(request):
    user = request.user
    news_feed = User.objects.get_news_feed_items_for_user(user=user)
    pictures = {}
    request_user = User.objects.get(user=request.user)
    for user in news_feed:
        for item in user.pictures.all():
            try:
                like = Like.objects.get(user=request_user, picture=item)
                liked = True
            except Like.DoesNotExist:
                liked = False
            pictures[item] = (user, liked)
    qs = OrderedDict(sorted(pictures.items(), key=lambda instance: instance[0].time_created, reverse=True))
    context = {
        'posts': qs,
    }
    return render(request, 'news_feed.html', context)


def user_profile(request, username):
    django_user = get_object_or_404(DjangoUser, username=username)
    user = get_object_or_404(User, user=django_user)
    request_user = User.objects.get(user=request.user)
    if request_user in user.followers.all():
        followed = True
    else:
        followed = False
    context = {
        'user': user,
        'followed': followed,
    }
    return render(request, 'user_profile.html', context)


def toggle_like(request):
    if request.method == 'POST':
        picture_id = request.POST['instance']
        user = User.objects.get(user=request.user)
        picture = Picture.objects.get(id=picture_id)
        like, created = Like.objects.get_or_create(picture=picture, user=user)
        if created:
            like.save()
        else:
            like.delete()
        response_data = {}
        return JsonResponse(response_data)


def toggle_follow(request):
    if request.method == 'POST':
        target_user = User.objects.get(user=DjangoUser.objects.get(id=request.POST['target_user']))
        user = User.objects.get(user=request.user)
        if user in target_user.followers.all():
            target_user.followers.remove(user)
        else:
            target_user.followers.add(user)
        target_user.save()
        response_data = {}
        return JsonResponse(response_data)


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


class RegistrationView():
    @staticmethod
    def get_success_view():   # redirects the user on submitting an account registration
        return "/"
