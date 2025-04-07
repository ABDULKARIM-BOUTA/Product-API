from products.models import Product
from rest_framework import serializers

def validate_name(value, instance=None):
    """
    Validate that the product name is unique, excluding the current instance if updating.
    """
    product_id = instance.pk if instance else None
    print(f"Validating product name: {value}, excluding instance: {product_id}")  # Debug line

    # Query products with the same name (case-insensitive)
    queryset = Product.objects.filter(name__iexact=value)

    if product_id:
        queryset = queryset.exclude(pk=product_id)  # Exclude the current product if updating

    print(f"Queryset count after exclusion: {queryset.count()}")  # Debug line

    # If another product with the same name exists, raise an error
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