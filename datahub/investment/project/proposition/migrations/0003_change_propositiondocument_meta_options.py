# Generated by Django 2.0.8 on 2018-08-10 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposition', '0002_propositiondocument'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propositiondocument',
            options={'default_permissions': ('add_all', 'change_all', 'delete'), 'permissions': (('read_all_propositiondocument', 'Can read all proposition document'), ('read_associated_propositiondocument', 'Can read proposition document for associated investment projects'), ('add_associated_propositiondocument', 'Can add proposition document for associated investment projects'), ('change_associated_propositiondocument', 'Can change proposition document for associated investment projects'), ('deleted_associated_propositiondocument', 'Can delete proposition document for associated investment projects')), 'verbose_name': 'investment project proposition document'},
        ),
    ]
