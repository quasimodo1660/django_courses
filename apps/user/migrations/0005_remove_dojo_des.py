# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_dojo_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='des',
        ),
    ]
