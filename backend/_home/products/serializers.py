from rest_framework import serializers
from products.models import Product
from products import validators
from api.serializers import UserDataSerializer
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)


class ProductSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(write_only=True)
    #url = serializers.HyperlinkedIdentityField(view_name="products:product-detail", lookup_field='pk')
    update_product = serializers.HyperlinkedIdentityField(view_name='products:product-update', lookup_field='pk')
    name = serializers.CharField(validators=[validators.validate_name_no_email])
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            #'email',
            #'url',
            'pk',
            'name',
            'price',
            'sale_price',
            'description',
            'path',
            'endpoint',
            'update_product',
            'user',
        ]

    def validate_name(self, value):
        try:
            product_id = self.instance.pk if self.instance else None
            queryset = Product.objects.filter(name__iexact=value)
            if product_id:
                queryset = queryset.exclude(pk=product_id)
            if queryset.exists():
                raise ValidationError(f'{value} already exists')
        except Exception as e:
            logger.error(f"Validation failed for product name '{value}': {str(e)}")
            raise
        return value



        # """
        # check that the product name is unique. Had to put it in the class serializer to exclude update from the unique constraint.
        # """
        # product_id = self.instance.pk if self.instance else None
        #
        # # Query products with the same name (case-insensitive)
        # queryset = Product.objects.filter(name__iexact=value)
        #
        # # Exclude the current product if updating
        # if product_id:
        #     queryset = queryset.exclude(pk=product_id)
        #
        # # If another product with the same name exists, raise an error
        # if queryset.exists():
        #     raise ValidationError(f'{value} already exists')
        #
        # return value

    # def create(self, validated_data):
    #     # Remove email before creation
    #     validated_data.pop('email')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     # Remove email before creation
    #     validated_data.pop('email')
    #     return super().update(instance, validated_data)