from products.serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from products.models import Product
from api.mixins import StaffEditorPermissionMixin

class ProductDetailAPIView(StaffEditorPermissionMixin, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIView(StaffEditorPermissionMixin, ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(StaffEditorPermissionMixin, UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteAPIView(StaffEditorPermissionMixin, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductListMixinView(ListModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
# class ProductDetailMixinView(RetrieveModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         return self.retrieve(request, *args, **kwargs)
#
# class ProductCreateMixinView(CreateModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ProductUpdateMixinView(UpdateModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         return self.update(request,*args, **kwargs)
#
# class ProductDeleteMixinView(DestroyModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         return self.destroy(request, *args, **kwargs)