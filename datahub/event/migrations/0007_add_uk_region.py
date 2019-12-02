# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_add_organiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='uk_region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.UKRegion'),
        ),
    ]
