# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20171213_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='dojo',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='user',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Dojo',
        ),
        migrations.DeleteModel(
            name='Ninja',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
