# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-23 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibouser',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
    ]
