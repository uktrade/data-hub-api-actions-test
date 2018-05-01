from logging import getLogger

from django.core.paginator import Paginator
from django.db import models

from datahub.search.apps import get_search_apps
from datahub.search.elasticsearch import bulk

logger = getLogger(__name__)

DEFAULT_BATCH_SIZE = 600


def get_datasets(models=None):
    """
    Returns datasets that will be synchronised with Elasticsearch.

    :param models: list of search app names to index, None for all
    """
    search_apps = get_search_apps()

    # if models empty, assume all models
    if not models:
        models = [search_app.name for search_app in search_apps]

    return [
        search_app.get_dataset()
        for search_app in search_apps
        if search_app.name in models
    ]


def _batch_rows(qs, batch_size=DEFAULT_BATCH_SIZE):
    """Yields QuerySet in chunks."""
    paginator = Paginator(qs, batch_size)
    for page in range(1, paginator.num_pages + 1):
        yield paginator.page(page).object_list


def sync_dataset(item, batch_size=DEFAULT_BATCH_SIZE):
    """Sends dataset to ElasticSearch in batches of batch_size."""
    model_name = item.es_model.__name__
    logger.info(f'Processing {model_name} records...')

    rows_processed = 0
    total_rows = (
        item.queryset.count()
        if isinstance(item.queryset, models.query.QuerySet) else len(item.queryset)
    )
    batches_processed = 0
    batches = _batch_rows(item.queryset, batch_size=batch_size)
    for batch in batches:
        actions = list(item.es_model.dbmodels_to_es_documents(batch))
        num_actions = len(actions)
        bulk(
            actions=actions,
            chunk_size=num_actions,
            request_timeout=300,
            raise_on_error=True,
            raise_on_exception=True,
        )

        rows_processed += num_actions
        batches_processed += 1
        if batches_processed % 100 == 0:
            logger.info(f'{model_name} rows processed: {rows_processed}/{total_rows} '
                        f'{rows_processed*100//total_rows}%')

    logger.info(f'{model_name} rows processed: {rows_processed}/{total_rows} 100%.')