# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='')),
                ('description', models.CharField(default='', max_length=500, verbose_name='Picture description')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('logitude', models.FloatField(blank=True, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='users.User', verbose_name='Owner')),
                ('tags', models.ManyToManyField(blank=True, related_name='pictures', to='tags.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.AlterOrderWithRespectTo(
            name='picture',
            order_with_respect_to='owner',
        ),
    ]
