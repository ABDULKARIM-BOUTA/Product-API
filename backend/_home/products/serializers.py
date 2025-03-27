from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="products:product-detail", lookup_field='pk')

    class Meta:
        model = Product
        fields = [
            'url',
            'pk',
            'name',
            'price',
            'sale_price',
        ]
