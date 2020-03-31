# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-24 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200224_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=64, verbose_name='课程名称')),
            ],
            options={
                'verbose_name': '课程表信息',
                'db_table': 'course',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-updated_at'], 'verbose_name': '学生表基本信息'},
        ),
    ]