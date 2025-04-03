# client.py
from algoliasearch.search.client import SearchClient
from django.conf import settings

def get_client():
    return SearchClient.create(settings.ALGOLIA_APP_ID, settings.ALGOLIA_ADMIN_KEY)

def get_index(index_name='cfe_Product'):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query, **kwargs):
    """
    perform_search("hello", tags=["electronics"], public=True)
    """
    index = get_index()
    search_params = {}
    filters = []

    tags = kwargs.pop("tags", None)
    if tags:
        filters.append(f"category:{tags}")  # Assuming 'category' is the attribute for tags

    public = kwargs.pop("public", None)
    if public is not None:
        filters.append(f"public:{public}")

    if filters:
        search_params["filters"] = " AND ".join(filters) #combine all filters using AND

    print(search_params)
    results = index.search(query, search_params)
    return results