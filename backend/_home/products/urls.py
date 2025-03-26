from django.urls import path
from products.views import ProductDetailAPIView, ProductListCreateAPIView
app_name = 'products'

urlpatterns = [
    path('create-list/', ProductListCreateAPIView.as_view()),
    path('<int:pk>/detail/', ProductDetailAPIView.as_view()),
]