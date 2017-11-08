# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 17:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_blog', '0005_rated_users_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_blog.Blog')),
            ],
        ),
    ]
