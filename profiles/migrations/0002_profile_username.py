# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
