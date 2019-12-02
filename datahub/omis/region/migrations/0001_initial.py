# Generated by Django 2.0.2 on 2018-02-07 13:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0001_squashed_0010_auto_20180613_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='UKRegionalSettings',
            fields=[
                ('uk_region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='omis_settings', serialize=False, to='metadata.UKRegion')),
                ('manager_emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, help_text='Comma-separated list of email addresses.', size=None)),
            ],
            options={
                'verbose_name': 'OMIS UK regional settings',
                'verbose_name_plural': 'OMIS UK regional settings',
            },
        ),
    ]
