# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 09:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metadata', '0001_squashed_0011_add_default_id_for_metadata'),
        ('company', '0001_squashed_0010_auto_20170807_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessLead',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('archived_on', models.DateTimeField(null=True)),
                ('archived_reason', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('job_title', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('trading_name', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('address_town', models.CharField(blank=True, max_length=255, null=True)),
                ('address_county', models.CharField(blank=True, max_length=255, null=True)),
                ('address_postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_alternative', models.CharField(blank=True, max_length=255, null=True)),
                ('email_alternative', models.EmailField(blank=True, max_length=254, null=True)),
                ('contactable_by_dit', models.BooleanField(default=False)),
                ('contactable_by_dit_partners', models.BooleanField(default=False)),
                ('contactable_by_email', models.BooleanField(default=False)),
                ('contactable_by_phone', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('address_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.Country')),
                ('advisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_leads', to=settings.AUTH_USER_MODEL)),
                ('archived_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_leads', to='company.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
