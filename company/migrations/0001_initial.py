# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 15:13
from __future__ import unicode_literals

import core.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(db_index=True, primary_key=True, serialize=False)),
                ('company_number', models.CharField(db_index=True, max_length=255, null=True)),
                ('uk_based', models.NullBooleanField(default=True)),
                ('trading_name', models.CharField(max_length=255, null=True)),
                ('website', models.URLField(null=True)),
                ('trading_address_1', models.CharField(max_length=255, null=True)),
                ('trading_address_2', models.CharField(max_length=255, null=True)),
                ('trading_address_town', models.CharField(max_length=255, null=True)),
                ('trading_address_county', models.CharField(max_length=255, null=True)),
                ('trading_address_country', models.CharField(max_length=255, null=True)),
                ('trading_address_postcode', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('business_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.BusinessType')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CompanyHouseCompany',
            fields=[
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('company_number', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('registered_address_care_of', models.CharField(blank=True, max_length=255)),
                ('registered_address_po_box', models.CharField(blank=True, max_length=255)),
                ('registered_address_address_1', models.CharField(blank=True, max_length=255)),
                ('registered_address_address_2', models.CharField(blank=True, max_length=255)),
                ('registered_address_town', models.CharField(blank=True, max_length=255)),
                ('registered_address_county', models.CharField(blank=True, max_length=255)),
                ('registered_address_country', models.CharField(blank=True, max_length=255)),
                ('registered_address_postcode', models.CharField(blank=True, max_length=255)),
                ('company_category', models.CharField(blank=True, max_length=255)),
                ('company_status', models.CharField(blank=True, max_length=255)),
                ('sic_code_1', models.CharField(blank=True, max_length=255)),
                ('sic_code_2', models.CharField(blank=True, max_length=255)),
                ('sic_code_3', models.CharField(blank=True, max_length=255)),
                ('sic_code_4', models.CharField(blank=True, max_length=255)),
                ('uri', models.CharField(blank=True, max_length=255)),
                ('incorporation_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(db_index=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('address_town', models.CharField(blank=True, max_length=255)),
                ('address_county', models.CharField(blank=True, max_length=255)),
                ('address_country', models.CharField(blank=True, max_length=255)),
                ('address_postcode', models.CharField(blank=True, max_length=255)),
                ('alt_phone', models.CharField(blank=True, max_length=255)),
                ('alt_email', models.EmailField(max_length=254, null=True)),
                ('notes', models.TextField(blank=True)),
                ('primary_contact_team', models.TextField(blank=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EmployeeRange',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(db_index=True, primary_key=True, serialize=False)),
                ('subject', models.TextField(blank=True)),
                ('date_of_interaction', models.DateTimeField()),
                ('notes', models.TextField(blank=True)),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Advisor')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Contact')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InteractionType',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TurnoverRange',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UKRegion',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.mixins.ReadOnlyModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='interaction',
            name='interaction_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.InteractionType'),
        ),
        migrations.AddField(
            model_name='contact',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Role'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Title'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='employee_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.EmployeeRange'),
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Sector'),
        ),
        migrations.AddField(
            model_name='company',
            name='turnover_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.TurnoverRange'),
        ),
        migrations.AddField(
            model_name='company',
            name='uk_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.UKRegion'),
        ),
    ]
