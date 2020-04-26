# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-04-26 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=32, verbose_name='学生姓名')),
                ('subject_name', models.CharField(max_length=32, verbose_name='科目')),
                ('score', models.FloatField(default=0, verbose_name='分数')),
                ('year', models.SmallIntegerField(verbose_name='年份')),
            ],
            options={
                'db_table': 'grade',
            },
        ),
    ]
