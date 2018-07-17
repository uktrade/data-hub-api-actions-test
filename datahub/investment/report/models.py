import uuid

from django.conf import settings
from django.db import models

from datahub.core.models import BaseModel
from datahub.core.utils import sign_s3_url, StrEnum
from datahub.investment.report.utils import get_report_s3_client

MAX_LENGTH = settings.CHAR_FIELD_MAX_LENGTH


class SPIReportPermission(StrEnum):
    """
    Permission codename constants.

    The following codename means that the user can read any type of spi report:

    change_spireport

    SPI reports are programmatically generated.

    TODO: should be replaced with view permission once Django 2.1 is available
    """

    change = 'change_spireport'


class SPIReport(BaseModel):
    """Investment Project SPI Report."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    s3_key = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'SPI report'
        default_permissions = (
            'change',
        )

    def get_absolute_url(self):
        """Generate pre-signed download URL."""
        return sign_s3_url(settings.REPORT_BUCKET, self.s3_key, client=get_report_s3_client())