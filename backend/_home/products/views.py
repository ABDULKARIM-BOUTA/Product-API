from products.serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from products.models import Product
from api.mixins import StaffEditorPermissionMixin

class ProductListCreateAPIView(StaffEditorPermissionMixin, ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #the user who created the product is assigned to the product by default
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()

        if user.is_superuser:
            return Product.objects.all()

        return Product.objects.filter(user=user)

class ProductDetailAPIView(StaffEditorPermissionMixin, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()

        if user.is_superuser:
            return Product.objects.all()

        return Product.objects.filter(user=user)

class ProductUpdateAPIView(StaffEditorPermissionMixin, RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()

        if user.is_superuser:
            return Product.objects.all()

        return Product.objects.filter(user=user)

class ProductDeleteAPIView(StaffEditorPermissionMixin, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()

        if user.is_superuser:
            return Product.objects.all()

        return Product.objects.filter(user=user)

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