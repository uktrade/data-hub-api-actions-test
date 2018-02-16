from logging import getLogger

import reversion

from datahub.dbmaintenance.utils import parse_bool, parse_date, parse_uuid
from datahub.investment.models import InvestmentProject
from ..base import CSVBaseCommand


logger = getLogger(__name__)


class Command(CSVBaseCommand):
    """
    Command to update investment_project.estimated_land_date and
    investment_project.allow_blank_estimated_land_date.
    """

    def add_arguments(self, parser):
        """Define extra arguments."""
        super().add_arguments(parser)
        parser.add_argument(
            '--simulate',
            action='store_true',
            dest='simulate',
            default=False,
            help='If True it only simulates the command without saving the changes.',
        )

    def _process_row(self, row, simulate=False, **options):
        """Process one single row."""
        pk = parse_uuid(row['id'])
        investment_project = InvestmentProject.objects.get(pk=pk)
        allow_blank_estimated_land_date = parse_bool(row['allow_blank_estimated_land_date'])
        estimated_land_date = parse_date(row['estimated_land_date'])

        if (investment_project.allow_blank_estimated_land_date == allow_blank_estimated_land_date
                and investment_project.estimated_land_date == estimated_land_date):
            return

        investment_project.allow_blank_estimated_land_date = allow_blank_estimated_land_date
        investment_project.estimated_land_date = estimated_land_date

        if simulate:
            return

        with reversion.create_revision():
            investment_project.save(
                update_fields=('estimated_land_date', 'allow_blank_estimated_land_date')
            )
            reversion.set_comment('Estimated land date migration correction.')