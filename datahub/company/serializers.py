from django.conf import settings

from rest_framework import serializers

from datahub.core.serializers import NestedRelatedField
from datahub.interaction.models import Interaction
from datahub.metadata import models as meta_models
from datahub.metadata.serializers import NestedCountrySerializer

from .models import Advisor, CompaniesHouseCompany, Company, Contact


class NestedContactSerializer(serializers.ModelSerializer):
    """Nested Contact serializer."""

    class Meta:  # noqa: D101
        model = Contact
        depth = 1
        fields = '__all__'


class NestedInteractionSerializer(serializers.ModelSerializer):
    """Nested Interaction Serializer."""

    class Meta:  # noqa: D101
        model = Interaction
        fields = '__all__'


class CompaniesHouseCompanySerializer(serializers.ModelSerializer):
    """Companies House company serializer."""

    class Meta:  # noqa: D101
        model = CompaniesHouseCompany
        depth = 1
        fields = '__all__'


class AdviserSerializer(serializers.ModelSerializer):
    """Adviser serializer."""

    name = serializers.CharField()

    class Meta:  # noqa: D101
        model = Advisor
        exclude = ('is_staff', 'is_active', 'date_joined', 'password')
        depth = 1


class CompanySerializerRead(serializers.ModelSerializer):
    """Company serializer."""

    name = serializers.SerializerMethodField('get_registered_name')
    trading_name = serializers.CharField(source='alias')
    companies_house_data = CompaniesHouseCompanySerializer()
    interactions = NestedInteractionSerializer(many=True)
    contacts = NestedContactSerializer(many=True)
    export_to_countries = NestedCountrySerializer(many=True)
    future_interest_countries = NestedCountrySerializer(many=True)
    uk_based = serializers.BooleanField()
    account_manager = AdviserSerializer()
    registered_address_1 = serializers.SerializerMethodField()
    registered_address_2 = serializers.SerializerMethodField()
    registered_address_3 = serializers.SerializerMethodField()
    registered_address_4 = serializers.SerializerMethodField()
    registered_address_town = serializers.SerializerMethodField()
    registered_address_country = serializers.SerializerMethodField()
    registered_address_county = serializers.SerializerMethodField()
    registered_address_postcode = serializers.SerializerMethodField()

    class Meta:  # noqa: D101
        model = Company
        depth = 1
        fields = '__all__'

    @staticmethod
    def _address_partial(obj, attr):
        """Return the address partial from obj."""
        obj = obj.companies_house_data or obj
        return getattr(obj, attr)

    @staticmethod
    def get_registered_name(obj):
        """Use the CH name, if there's one, else the name."""
        return obj.companies_house_data.name if obj.companies_house_data else obj.name

    def get_registered_address_1(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_1')

    def get_registered_address_2(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_2')

    def get_registered_address_3(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_3')

    def get_registered_address_4(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_4')

    @staticmethod
    def get_registered_address_country(obj):
        """Return CH address if present."""
        obj = obj.companies_house_data or obj
        if obj.registered_address_country:
            return {'id': str(obj.registered_address_country.id), 'name': obj.registered_address_country.name}
        else:
            return {}

    def get_registered_address_county(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_county')

    def get_registered_address_postcode(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_postcode')

    def get_registered_address_town(self, obj):
        """Return CH address if present."""
        return self._address_partial(obj, 'registered_address_town')


class CompanySerializerWrite(serializers.ModelSerializer):
    """Company serializer for writing operations."""

    classification = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:  # noqa: D101
        model = Company
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer for writing operations V3."""

    title = NestedRelatedField(
        meta_models.Title, required=False, allow_null=True
    )
    company = NestedRelatedField(
        Company, required=False, allow_null=True
    )
    adviser = NestedRelatedField(
        Advisor, read_only=True,
        extra_fields=('first_name', 'last_name')
    )
    address_country = NestedRelatedField(
        meta_models.Country, required=False, allow_null=True
    )
    archived = serializers.BooleanField(read_only=True)
    archived_on = serializers.DateTimeField(read_only=True)
    archived_reason = serializers.CharField(read_only=True)
    archived_by = NestedRelatedField(
        settings.AUTH_USER_MODEL, read_only=True,
        extra_fields=('first_name', 'last_name')
    )

    class Meta:  # noqa: D101
        model = Contact
        fields = (
            'id', 'title', 'first_name', 'last_name', 'job_title', 'company', 'adviser',
            'primary', 'telephone_countrycode', 'telephone_number', 'email',
            'address_same_as_company', 'address_1', 'address_2', 'address_3', 'address_4',
            'address_town', 'address_county', 'address_country', 'address_postcode',
            'telephone_alternative', 'email_alternative', 'notes', 'contactable_by_dit',
            'contactable_by_dit_partners', 'contactable_by_email', 'contactable_by_phone',
            'archived', 'archived_on', 'archived_reason', 'archived_by', 'created_on'
        )
