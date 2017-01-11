# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=4000)),
                ('rating', models.CharField(max_length=1, choices=[(b'1', b'Bliss'), (b'2', b'Good'), (b'3', b'Neutral'), (b'4', b'Bad'), (b'5', b'Nightmare')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50)),
                ('dream', models.ManyToManyField(to='tracer.Dream')),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=50)),
                ('dream', models.ManyToManyField(to='tracer.Dream')),
            ],
        ),
    ]
