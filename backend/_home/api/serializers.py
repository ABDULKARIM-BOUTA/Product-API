from rest_framework import serializers

# nested serializer to show product's info of a specific user
class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="products:product-detail", lookup_field='pk', read_only=True)
    name = serializers.CharField(read_only=True)

# nested serializer to show user's info in the product
class UserDataSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        qs = obj.product_set.all()[:3]
        return UserProductInlineSerializer(qs, many=True, context=self.context).data