# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0002_auto_20170116_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 1, 16, 22, 38, 41, 924000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
