from django.urls import path
from products.views import ProductDetailAPIView, ProductCreateAPIView, ProductDeleteAPIView, ProductUpdateAPIView, ProductListApiView

app_name = 'products'

urlpatterns = [
    path('list/', ProductListApiView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/detail/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
]