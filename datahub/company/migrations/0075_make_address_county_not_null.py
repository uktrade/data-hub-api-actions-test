# Generated by Django 2.2 on 2019-04-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0074_make_address_town_not_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address_county',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
    ]
