from datahub.core.validate_utils import DataCombiner
from datahub.investment.investor_profile.models import LargeCapitalInvestorProfile
from datahub.investment.validate import field_incomplete


def get_incomplete_fields(instance, fields):
    """Returns a list of fields that are incomplete."""
    combiner = DataCombiner(instance, {}, model=LargeCapitalInvestorProfile)
    incomplete_fields = []
    for field in fields:
        if field_incomplete(combiner, field):
            incomplete_fields.append(field)
    return incomplete_fields
