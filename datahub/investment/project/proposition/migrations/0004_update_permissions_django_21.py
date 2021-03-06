# Generated by Django 2.1 on 2018-08-10 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposition', '0003_change_propositiondocument_meta_options'),
        ('core', '0003_rename_read_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proposition',
            options={'default_permissions': ('add_all', 'change_all', 'delete'), 'permissions': (('view_all_proposition', 'Can view all proposition'), ('view_associated_investmentproject_proposition', 'Can view proposition for associated investment projects'), ('add_associated_investmentproject_proposition', 'Can add proposition for associated investment projects'), ('change_associated_investmentproject_proposition', 'Can change proposition for associated investment projects'))},
        ),
        migrations.AlterModelOptions(
            name='propositiondocument',
            options={'default_permissions': ('add_all', 'change_all', 'delete'), 'permissions': (('view_all_propositiondocument', 'Can view all proposition document'), ('view_associated_propositiondocument', 'Can view proposition document for associated investment projects'), ('add_associated_propositiondocument', 'Can add proposition document for associated investment projects'), ('change_associated_propositiondocument', 'Can change proposition document for associated investment projects'), ('deleted_associated_propositiondocument', 'Can delete proposition document for associated investment projects')), 'verbose_name': 'investment project proposition document'},
        ),
    ]
