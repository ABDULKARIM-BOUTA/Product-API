from django.urls import path
from products.views import ProductDetailAPIView, ProductListCreateAPIView, ProductDeleteAPIView, ProductUpdateAPIView #ProductListMixinView, ProductDetailMixinView, ProductCreateMixinView, ProductUpdateMixinView, ProductDeleteMixinView

app_name = 'products'

urlpatterns = [
    path('list-create/', ProductListCreateAPIView.as_view()),
    path('<int:pk>/detail/', ProductDetailAPIView.as_view()),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view()),
]