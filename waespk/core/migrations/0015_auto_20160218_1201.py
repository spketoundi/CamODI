# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.models
import django.db.models.deletion
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('ossuo', '0014_workpage_show_in_play_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='ossuoimage',
            name='file_size',
            field=models.PositiveIntegerField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='file',
            field=models.ImageField(height_field='height', upload_to=wagtail.wagtailimages.models.get_upload_to, width_field='width', verbose_name='file'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='height',
            field=models.IntegerField(verbose_name='height', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=None, verbose_name='tags'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='uploaded_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='uploaded by user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ossuoimage',
            name='width',
            field=models.IntegerField(verbose_name='width', editable=False),
            preserve_default=True,
        ),
    ]
