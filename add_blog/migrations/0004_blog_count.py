# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_blog', '0003_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
