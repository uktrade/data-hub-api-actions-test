from enum import Enum
from uuid import UUID

from datahub.core.constants import Constant


NOTIFY_DNB_INVESTIGATION_FEATURE_FLAG = 'notify-dnb-investigations'
AUTOMATIC_COMPANY_ARCHIVE_FEATURE_FLAG = 'automatic-company-archive'
EXPORT_COUNTRIES_FEATURE_FLAG = 'export-countries-switch'
UPDATE_CONSENT_SERVICE_FEATURE_FLAG = 'update-consent-service'
GET_CONSENT_FROM_CONSENT_SERVICE = 'get-consent-from-consent-service'

CONSENT_SERVICE_EMAIL_CONSENT_TYPE = 'email_marketing'


class BusinessTypeConstant(Enum):
    """
    Business type constants.

    Note:
        These are automatically loaded to the database via a post_migrate signal receiver (which
        runs whenever the migrate command is run).
        The signal receiver only creates and updates business types; it does not delete them.
        See datahub.company.signals for the implementation.

    """

    charity = Constant('Charity', '9dd14e94-5d95-e211-a939-e4115bead28a')
    company = Constant('Company', '98d14e94-5d95-e211-a939-e4115bead28a')
    government_dept_or_other_public_body = Constant(
        'Government department or other public body',
        '9cd14e94-5d95-e211-a939-e4115bead28a',
    )
    intermediary = Constant('Intermediary', '9bd14e94-5d95-e211-a939-e4115bead28a')
    limited_partnership = Constant(
        'Limited partnership', '8b6eaf7e-03e7-e611-bca1-e4115bead28a',
    )
    limited_liability_partnership = Constant(
        'Limited liability partnership', 'b70764b9-e523-46cf-8297-4c694ecbc5ce',
    )
    partnership = Constant('Partnership', '9ad14e94-5d95-e211-a939-e4115bead28a')
    sole_trader = Constant('Sole Trader', '99d14e94-5d95-e211-a939-e4115bead28a')
    private_limited_company = Constant(
        'Private limited company', '6f75408b-03e7-e611-bca1-e4115bead28a',
    )
    public_limited_company = Constant(
        'Public limited company', 'dac8c591-03e7-e611-bca1-e4115bead28a',
    )
    # These are called UK establishments by Companies House and in law, but we are calling them
    # branches in the front end.
    uk_establishment = Constant(
        'UK branch of foreign company (BR)', 'b0730fc6-fcce-4071-bdab-ba8de4f4fc98',
    )
    community_interest_company = Constant(
        'Community interest company', '34e4cb83-e5e1-421e-ac90-8a52edcc209c',
    )


class OneListTierID(Enum):
    """One List tier IDs."""

    tier_d_international_trade_advisers = UUID('1929c808-99b4-4abf-a891-45f2e187b410')
