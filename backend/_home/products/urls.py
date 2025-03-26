from django.urls import path
from products.views import ProductDetailAPIView, ProductCreateAPIView

app_name = 'products'

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view()),
    path('<int:pk>/detail/', ProductDetailAPIView.as_view()),
]