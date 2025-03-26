from products.serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from products.models import Product

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer