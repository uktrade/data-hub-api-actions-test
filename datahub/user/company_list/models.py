from uuid import uuid4

from django.conf import settings
from django.db import models
from django.db.models import Q

from datahub.core.models import BaseModel
from datahub.core.utils import StrEnum


class CompanyList(BaseModel):
    """A user-created list of companies."""

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    adviser = models.ForeignKey(
        'company.Advisor',
        on_delete=models.CASCADE,
        related_name='company_lists',
    )
    # TODO: Remove this once the legacy company list functionality has been removed
    is_legacy_default = models.BooleanField(
        default=False,
        help_text='Temporary field that designates this as the list that the legacy company list '
                  'API endpoints operate on.',
    )

    def __str__(self):
        """Human-friendly representation."""
        return f'{self.name} – {self.adviser}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('adviser',),
                condition=Q(is_legacy_default=True),
                name='unique_adviser_if_legacy_default',
            ),
            # While CompanyListItem.list is still being populated for existing objects,
            # is_legacy_default=False is not allowed
            models.CheckConstraint(
                check=Q(is_legacy_default=True),
                name='disallow_is_legacy_default_false',
            ),
        ]


class CompanyListItemPermissionCode(StrEnum):
    """CompanyListItem permission codename constants."""

    view_company_list_item = 'view_companylistitem'
    add_company_list_item = 'add_companylistitem'
    change_company_list_item = 'change_companylistitem'
    delete_company_list_item = 'delete_companylistitem'


class CompanyListItem(BaseModel):
    """
    An item on a user's personal list of companies.

    Each company can appear only once for a particular user.

    Note that the primary key is not exposed via the API.
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    adviser = models.ForeignKey(
        'company.Advisor',
        on_delete=models.CASCADE,
        related_name='company_list_items',
    )
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        related_name='company_list_items',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('adviser', 'company'),
                name='unique_adviser_and_company',
            ),
        ]
        indexes = [
            models.Index(fields=('adviser', 'company')),
        ]
