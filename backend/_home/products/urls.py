from django.urls import path
from products.views import (ProductDetailAPIView, ProductListCreateAPIView, ProductDeleteAPIView, ProductUpdateAPIView, ProductListMixinView, ProductDetailMixinView, ProductCreateMixinView, ProductUpdateMixinView, ProductDeleteMixinView)

app_name = 'products'

urlpatterns = [
    path('list/', ProductListMixinView.as_view()),
    path('create/', ProductCreateMixinView.as_view()),
    path('<int:pk>/detail/', ProductDetailMixinView.as_view()),
    path('<int:pk>/update/', ProductUpdateMixinView.as_view()),
    path('<int:pk>/delete/', ProductDeleteMixinView.as_view()),
]