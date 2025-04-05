from algoliasearch.search.client import SearchClientSync
from django.conf import settings

def get_client():
    """
    Get the client instance using Algolia Application ID and API Key from Django settings.
    """
    client = SearchClientSync(settings.ALGOLIA['APPLICATION_ID'], settings.ALGOLIA['API_KEY'])
    return client

def perform_search(query, **kwargs):
    """
    Perform a search query with optional filters like tags and public status.
    """
    # Initialize the Algolia client
    client = get_client()

    # Prepare the search parameters
    params = {"query": query}

    # Debugging the filters
    print(f"Filters before applying: {kwargs}")

    # Add tag filters if provided
    tags = kwargs.get('tags', [])
    if tags:
        params['tagFilters'] = tags
        print(f"Adding tagFilters: {tags}")

    # Check the final query parameters
    print(f"Search Params without facetFilters: {params}")

    # Perform the search on the specified index
    try:
        search_response = client.search_single_index('Product', params)

        # Extract the hits and format the data
        hits = search_response.hits
        results = []

        # Clean up each hit and remove unnecessary metadata
        for hit in hits:
            hit_data = {
                "name": hit.name,
                "price": hit.price,
                "sale_price": hit.sale_price,
                "description": hit.description,
                "path": hit.path,
                "endpoint": hit.endpoint,
                "tags": hit._tags,
            }
            results.append(hit_data)

        # Handle case when there are no results
        if not results:
            return {"message": "No results found"}

        return {
            'hits': results,  # Cleaned-up hits data
            'total_hits': search_response.nb_hits,  # Total number of hits
            'page': search_response.page,  # Current page of the search results
            'hits_per_page': search_response.hits_per_page,  # Results per page
        }

    except Exception as e:
        # Handle any exceptions that may arise (e.g., connection errors)
        return {'error': str(e)}
