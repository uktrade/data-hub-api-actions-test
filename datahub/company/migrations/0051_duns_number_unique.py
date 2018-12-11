# Generated by Django 2.1.3 on 2018-12-07 14:23

import django.core.validators
from django.db import migrations, models
import re


def set_duns_number_to_null(apps, schema_editor):
    Company = apps.get_model('company', 'Company')
    Company.objects.filter(duns_number='').update(duns_number=None)


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0050_duns_number_remove_default'),
    ]

    operations = [
        # convert '' to null one more time, just in case, in order to avoid issues with unique=True.
        migrations.RunPython(set_duns_number_to_null, migrations.RunPython.noop, elidable=True),
        migrations.AlterField(
            model_name='company',
            name='duns_number',
            field=models.CharField(blank=True, help_text='Dun & Bradstreet unique identifier. Nine-digit number with leading zeros.', max_length=9, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9), django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.')]),
        ),
    ]
