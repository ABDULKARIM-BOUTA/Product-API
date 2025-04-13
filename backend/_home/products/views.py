#view
from products.serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from products.models import Product
from users.mixins import StaffEditorPermissionMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

class ProductListApiView(ListAPIView):
    # Anyone can access the list

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(cache_page(timeout=30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ProductCreateAPIView(CreateAPIView):
    # Ony registered users can create records

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        #the user who created the product is assigned to the product by default
        user = self.request.user
        serializer.save(user=user)

class ProductDetailAPIView(RetrieveAPIView):
    # Anyone can access record's details

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @method_decorator(cache_page(30))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductUpdateAPIView(StaffEditorPermissionMixin, RetrieveUpdateAPIView):


    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        # unauthenticated users cant view the items
        if not user.is_authenticated:
            return Product.objects.none()

        # superuser can view all the items
        if user.is_superuser:
            return Product.objects.all()

        # users can see only their items
        return Product.objects.filter(user=user)

class ProductDeleteAPIView(StaffEditorPermissionMixin, DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        # unauthenticated users cant view the items
        if not user.is_authenticated:
            return Product.objects.none()

        # superuser can view all the items
        if user.is_superuser:
            return Product.objects.all()

        # users can see only their items
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

# class ProductListCreateAPIView(ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
# 
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [AllowAny()]
#         return [IsAuthenticated()]
# 
#     def perform_create(self, serializer):
#         #the user who created the product is assigned to the product by default
#         user = self.request.user
#         if user.is_active:      # Ensure the user is active
#             serializer.save(user=user)
#         else:
#             raise PermissionDenied("Only active users can create products.")
# 
#     # caching for a minute
#     @method_decorator(cache_page(timeout=15))
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
