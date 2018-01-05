# Generated by Django 2.0.1 on 2018-01-03 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0011_add_default_id_for_metadata'),
        ('omis-invoice', '0003_adding_read_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='billing_address_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_address_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_address_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='metadata.Country'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_address_county',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_address_postcode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_address_town',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_company_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_contact_name',
            field=models.CharField(blank=True, editable=False, help_text='Legacy field. Billing contact name.', max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]