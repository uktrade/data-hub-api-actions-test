# Generated by Django 2.1.4 on 2019-03-04 09:19

from pathlib import PurePath

import django.core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from datahub.core.migration_utils import load_yaml_data_in_migration
import uuid


metadata_files = [
    'asset_class_interest_sector.yaml',
    'asset_class_interest.yaml',
    'required_checks_conducted.yaml',
    'construction_risk.yaml',
    'deal_ticket_size.yaml',
    'desired_deal_role.yaml',
    'equity_percentage.yaml',
    'investor_type.yaml',
    'large_capital_investment_type.yaml',
    'restriction.yaml',
    'return_rate.yaml',
    'time_horizon.yaml'
]


def load_metadata(apps, schema_editor):
    for file_name in metadata_files:
        load_yaml_data_in_migration(
            apps,
            PurePath(__file__).parent / f'0001_initial/{file_name}',
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_squashed_0096_company_global_ultimate_duns_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metadata', '0022_add_administrative_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetClassInterest',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetClassInterestSector',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConstructionRisk',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DealTicketSize',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DesiredDealRole',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EquityPercentage',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestorProfile',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('investable_capital', models.BigIntegerField(blank=True, help_text='Investable capital amount in USD', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('global_assets_under_management', models.BigIntegerField(blank=True, help_text='Global assets under management amount in USD', null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('investor_description', models.TextField(blank=True)),
                ('notes_on_locations', models.TextField(blank=True)),
                ('asset_classes_of_interest', models.ManyToManyField(blank=True, related_name='_investorprofile_asset_classes_of_interest_+', to='investor_profile.AssetClassInterest')),
                ('construction_risks', models.ManyToManyField(blank=True, related_name='_investorprofile_construction_risks_+', to='investor_profile.ConstructionRisk')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deal_ticket_sizes', models.ManyToManyField(blank=True, related_name='_investorprofile_deal_ticket_sizes_+', to='investor_profile.DealTicketSize')),
                ('desired_deal_roles', models.ManyToManyField(blank=True, related_name='_investorprofile_desired_deal_roles_+', to='investor_profile.DesiredDealRole')),
            ],
        ),
        migrations.CreateModel(
            name='InvestorType',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LargeCapitalInvestmentType',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequiredChecksConducted',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnRate',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeHorizon',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='investment_types',
            field=models.ManyToManyField(blank=True, related_name='_investorprofile_investment_types_+', to='investor_profile.LargeCapitalInvestmentType'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='investor_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_profiles', to='company.Company'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='investor_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='investor_profile.InvestorType'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='minimum_equity_percentage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='investor_profile.EquityPercentage'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='minimum_return_rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='investor_profile.ReturnRate'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='other_countries_being_considered',
            field=models.ManyToManyField(blank=True, help_text='The other countries being considered for investment', related_name='_investorprofile_other_countries_being_considered_+', to='metadata.Country'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='profile_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='investor_profile.ProfileType'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='required_checks_conducted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='investor_profile.RequiredChecksConducted'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='restrictions',
            field=models.ManyToManyField(blank=True, related_name='_investorprofile_restrictions_+', to='investor_profile.Restriction'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='time_horizons',
            field=models.ManyToManyField(blank=True, related_name='_investorprofile_time_horizons_+', to='investor_profile.TimeHorizon'),
        ),
        migrations.AddField(
            model_name='investorprofile',
            name='uk_region_locations',
            field=models.ManyToManyField(blank=True, related_name='_investorprofile_uk_region_locations_+', to='metadata.UKRegion', verbose_name='possible UK regions'),
        ),
        migrations.AddField(
            model_name='assetclassinterest',
            name='asset_class_interest_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_class_interests', to='investor_profile.AssetClassInterestSector'),
        ),
        migrations.AlterUniqueTogether(
            name='investorprofile',
            unique_together={('investor_company', 'profile_type')},
        ),
        migrations.RunPython(load_metadata, migrations.RunPython.noop),
    ]
