#index.py
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from products.models import Product

@register(Product)
# specify the data that the index will show
class ProductIndex(AlgoliaIndex):
    # if public is False the record will not show
    should_index = 'is_public'

    fields = [
        'name',
        'price',
        'description',
        'sale_price',
        'public',
        'path',
        'endpoint',
    ]
    tags = 'get_tags_list'

