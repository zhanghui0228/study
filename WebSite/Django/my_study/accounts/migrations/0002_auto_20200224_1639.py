# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-24 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生表基本信息'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
