# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-05 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_remove_dadospessoais_actual_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='github',
            field=models.CharField(default=b'http://github.com/SeuGit', max_length=100, verbose_name=b'Github'),
        ),
    ]
