# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-14 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180113_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.FileField(upload_to=''),
        ),
    ]
