# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0004_auto_20170512_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentproject',
            old_name='business_activity',
            new_name='business_activities',
        ),
    ]
