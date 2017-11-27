from oauth2_provider.contrib.rest_framework.permissions import IsAuthenticatedOrTokenHasScope
from rest_framework.response import Response
from rest_framework.views import APIView

from datahub.oauth.scopes import Scope
from datahub.search.contact.models import Contact
from datahub.search.elasticsearch import get_search_by_entity_query, limit_search_query
from datahub.search.interaction.models import Interaction
from .serializers import LimitParamSerializer


class IntelligentHomepageView(APIView):
    """Return the data for the intelligent homepage."""

    permission_classes = (IsAuthenticatedOrTokenHasScope,)

    required_scopes = (Scope.internal_front_end,)
    http_method_names = ['get']

    def get(self, request, format=None):
        """Implement GET method."""
        user = request.user
        serializer = LimitParamSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        limit = serializer.validated_data['limit']

        interactions_query = get_search_by_entity_query(
            term='',
            entity=Interaction,
            filters={
                'dit_adviser.id': user.id,
            },
            field_order='created_on:desc',
        )
        interactions = limit_search_query(
            interactions_query,
            offset=0,
            limit=limit,
        ).execute()

        contacts_query = get_search_by_entity_query(
            term='',
            entity=Contact,
            filters={
                'created_by.id': user.id,
            },
            field_order='created_on:desc',
        )
        contacts = limit_search_query(
            contacts_query,
            offset=0,
            limit=limit,
        ).execute()

        response = {
            'interactions': [interaction.to_dict() for interaction in interactions.hits],
            'contacts': [contact.to_dict() for contact in contacts],
        }
        return Response(data=response)
