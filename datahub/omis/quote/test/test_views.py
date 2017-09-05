import uuid
from unittest import mock
import pytest

from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse

from datahub.core.test_utils import APITestMixin
from datahub.omis.order.models import Order
from datahub.omis.order.test.factories import OrderFactory, OrderWithOpenQuoteFactory

from ..models import Quote

# mark the whole module for db use
pytestmark = pytest.mark.django_db


class TestCreatePreviewOrder(APITestMixin):
    """Tests for creating and previewing a quote."""

    @pytest.mark.parametrize('quote_view_name', ('item', 'preview'))
    def test_404_if_order_doesnt_exist(self, quote_view_name):
        """Test that if the order doesn't exist, the endpoint returns 404."""
        url = reverse(
            f'api-v3:omis:quote:{quote_view_name}',
            kwargs={'order_pk': uuid.uuid4()}
        )
        response = self.api_client.post(url, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.parametrize('quote_view_name', ('item', 'preview'))
    def test_409_if_theres_already_a_valid_quote(self, quote_view_name):
        """Test that if the order has already an active quote, the endpoint returns 409."""
        order = OrderWithOpenQuoteFactory()

        url = reverse(
            f'api-v3:omis:quote:{quote_view_name}',
            kwargs={'order_pk': order.pk}
        )
        response = self.api_client.post(url, format='json')

        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json() == {'detail': "There's already an active quote."}

    @pytest.mark.parametrize('quote_view_name', ('item', 'preview'))
    @pytest.mark.parametrize(
        'field,value',
        (
            ('service_types', []),
            ('description', ''),
            ('delivery_date', None),
        )
    )
    @freeze_time('2017-04-18 13:00:00.000000+00:00')
    def test_400_if_incomplete_order(self, quote_view_name, field, value):
        """If the order is incomplete, the quote cannot be generated."""
        order = OrderFactory(**{field: value})

        url = reverse(
            f'api-v3:omis:quote:{quote_view_name}',
            kwargs={'order_pk': order.pk}
        )
        response = self.api_client.post(url, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            field: ['This field is required.']
        }

    @freeze_time('2017-04-18 13:00:00.000000+00:00')
    def test_create_success(self):
        """Test a successful call to create a quote."""
        order = OrderFactory()

        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': order.pk})
        response = self.api_client.post(url, format='json')

        order.refresh_from_db()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'content': order.quote.content,
            'created_on': '2017-04-18T13:00:00',
            'created_by': {
                'id': str(self.user.pk),
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'name': self.user.name
            }
        }

        quote = Quote.objects.first()
        assert order.quote == quote

    def test_create_as_atomic_operation(self):
        """
        Test that if there's a problem when saving the order, the quote is not saved
        either so that we keep db integrity.
        """
        order = OrderFactory()

        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': order.pk})

        with mock.patch.object(Order, 'save') as mocked_save:
            mocked_save.side_effect = Exception()

            with pytest.raises(Exception):
                self.api_client.post(url, format='json')

        order.refresh_from_db()
        assert not order.quote
        assert not Quote.objects.count()

    def test_preview_success(self):
        """
        Test a successful call to preview a quote.
        Changes are not saved in the db.
        """
        order = OrderFactory()

        url = reverse('api-v3:omis:quote:preview', kwargs={'order_pk': order.pk})
        response = self.api_client.post(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert order.reference in response.json()['content']
        assert response.json() == {
            'content': response.json()['content'],
            'created_on': None,
            'created_by': None
        }

        order.refresh_from_db()
        assert not order.quote
        assert not Quote.objects.count()


class TestGetQuote(APITestMixin):
    """Get quote test case."""

    def test_get_basic(self):
        """Test a successful call to get a basic quote (without `expand` param)."""
        order = OrderWithOpenQuoteFactory()
        quote = order.quote

        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': order.pk})
        response = self.api_client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'created_on': quote.created_on.isoformat(),
            'created_by': {
                'id': str(quote.created_by.pk),
                'first_name': quote.created_by.first_name,
                'last_name': quote.created_by.last_name,
                'name': quote.created_by.name
            },

        }

    def test_get_expanded(self):
        """Test a successful call to get a quote and its content (with `expand` param)."""
        order = OrderWithOpenQuoteFactory()
        quote = order.quote

        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': order.pk})
        response = self.api_client.get(
            url,
            {'expand': True},
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'created_on': quote.created_on.isoformat(),
            'created_by': {
                'id': str(quote.created_by.pk),
                'first_name': quote.created_by.first_name,
                'last_name': quote.created_by.last_name,
                'name': quote.created_by.name
            },
            'content': quote.content
        }

    def test_400_with_invalid_expand_value(self):
        """Test if `expand` is not a boolean value, 400 is returned."""
        order = OrderWithOpenQuoteFactory()

        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': order.pk})
        response = self.api_client.get(
            url,
            {'expand': 'invalid-value'},
            format='json'
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            'expand': [
                '"invalid-value" is not a valid boolean.'
            ]
        }

    def test_404_if_order_doesnt_exist(self):
        """Test that if the order doesn't exist, the endpoint returns 404."""
        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': uuid.uuid4()})
        response = self.api_client.get(url, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_404_if_quote_doesnt_exist(self):
        """Test that if the quote doesn't exist, the endpoint returns 404."""
        order = OrderFactory()
        assert not order.quote

        url = reverse('api-v3:omis:quote:item', kwargs={'order_pk': order.pk})
        response = self.api_client.get(url, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND
