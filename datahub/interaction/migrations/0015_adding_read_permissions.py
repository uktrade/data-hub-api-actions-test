# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0014_remove_service_delivery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interaction',
            options={'permissions': (('read_interaction', 'Can read interaction'),)},
        ),
    ]