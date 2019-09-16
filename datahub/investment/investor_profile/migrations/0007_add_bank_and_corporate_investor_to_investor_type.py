# Generated by Django 2.2.4 on 2019-09-10 12:25

from pathlib import PurePath

from django.db import migrations
from datahub.core.migration_utils import load_yaml_data_in_migration


def load_metadata(apps, schema_editor):
    load_yaml_data_in_migration(
        apps,
        PurePath(__file__).parent /
        f'0007_add_bank_and_corporate_investor_to_investor_type/investor_type.yaml',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('investor_profile', '0006_fix_asset_class_spellings'),
    ]

    operations = [
        migrations.RunPython(load_metadata, migrations.RunPython.noop)
    ]