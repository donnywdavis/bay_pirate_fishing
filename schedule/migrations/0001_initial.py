# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('event', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('rank', models.CharField(max_length=50, blank=True)),
            ],
        ),
    ]
