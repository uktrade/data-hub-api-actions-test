# Generated by Django 2.2.6 on 2019-11-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_support', '0002_add_related_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplemodel',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
