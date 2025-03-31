from rest_framework import serializers
from products.models import Product
from products import validators

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="products:product-detail", lookup_field='pk')
    name = serializers.CharField(validators=[validators.validate_name, validators.validate_name_no_email])

    #email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            #'email',
            #'user',
            'url',
            'pk',
            'name',
            'price',
            'sale_price',
        ]

    # def create(self, validated_data):
    #     # Remove email before creation
    #     validated_data.pop('email')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     # Remove email before creation
    #     validated_data.pop('email')
    #     return super().update(instance, validated_data)