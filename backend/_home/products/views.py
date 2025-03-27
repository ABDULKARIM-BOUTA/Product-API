from products.serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from products.models import Product
from rest_framework import authentication, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from products.permissions import IsStaffEditorPermission

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Authentication and permission
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    # using a custom permission so a staff that does not have permission can not view the product list
    # classes order is important
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Authentication and permission
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Authentication and permission
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
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