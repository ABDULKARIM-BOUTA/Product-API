from rest_framework import serializers
from products.models import Product
from products import validators
from api.serializers import UserDataSerializer

class ProductSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(write_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="products:product-detail", lookup_field='pk')
    name = serializers.CharField(validators=[validators.validate_name, validators.validate_name_no_email])
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            #'email',
            'url',
            'user',
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