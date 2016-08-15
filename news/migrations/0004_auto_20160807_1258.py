# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=b'', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
