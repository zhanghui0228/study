# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-04-16 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0003_weibouser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibouser',
            name='creaete_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='创建时间'),
        ),
    ]
