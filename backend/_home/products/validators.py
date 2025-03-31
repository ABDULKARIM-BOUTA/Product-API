from products.models import Product
from rest_framework import serializers

def validate_name(value):
    # ensure a product has a unique name
    queryset = Product.objects.filter(name__iexact=value)
    if queryset.exists():
        raise serializers.ValidationError(f'{value} already exists')
    return value

def validate_name_no_email(value):
    # ensure user does not enter email
    if '@' in value.lower():
        raise serializers.ValidationError('@ is not allowed in names')

    elif '.com' in value.lower():
        raise serializers.ValidationError('.com is not allowed in names')
    return value