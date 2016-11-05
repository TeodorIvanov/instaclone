# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pictures', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('picture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pictures.Picture', verbose_name='Liked picture', related_name='likes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='Liked by user')),
            ],
        ),
    ]
