# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0003_auto_20170116_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='theme',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name=b'Themes'),
        ),
    ]
