# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161113_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(upload_to=''),
        ),
    ]