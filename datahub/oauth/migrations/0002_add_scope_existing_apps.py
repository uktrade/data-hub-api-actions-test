# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 08:11
from __future__ import unicode_literals

from django.db import migrations
from oauth2_provider.settings import oauth2_settings


def set_scopes_for_existing_apps(apps, schema_editor):
    Application = apps.get_model(oauth2_settings.APPLICATION_MODEL)
    OAuthApplicationScope = apps.get_model('oauth', 'OAuthApplicationScope')
    for application in Application.objects.all():
        try:
            OAuthApplicationScope.objects.get(application=application)
        except OAuthApplicationScope.DoesNotExist:
            OAuthApplicationScope.objects.create(
                application=application, scopes=['internal-front-end']
            )


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(oauth2_settings.APPLICATION_MODEL),
        ('oauth', '0001_add_oauth_app_scope'),
    ]

    operations = [
        migrations.RunPython(set_scopes_for_existing_apps, migrations.RunPython.noop, elidable=True),
    ]
