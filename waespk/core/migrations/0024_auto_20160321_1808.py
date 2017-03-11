# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossuo', '0023_marketinglandingpage_marketinglandingpagerelatedlink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketinglandingpage',
            options={'verbose_name': 'Marketing Landing Page'},
        ),
        migrations.AddField(
            model_name='blogpage',
            name='marketing_only',
            field=models.BooleanField(default=False, help_text='Display this blog post only on marketing landing page'),
        ),
        migrations.AddField(
            model_name='workpage',
            name='marketing_only',
            field=models.BooleanField(default=False, help_text='Display this work item only on marketing landing page'),
        ),
    ]
