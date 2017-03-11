# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossuo', '0018_auto_20160222_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleadgrantspage',
            name='to_address',
            field=models.EmailField(blank=True, help_text='Optional - form submissions will be emailed to this address', max_length=254, verbose_name='to address'),
        ),
    ]
