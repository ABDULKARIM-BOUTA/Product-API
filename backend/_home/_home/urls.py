from django.contrib import admin
from django.urls import path, include
from products.views import ProductListCreateAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListCreateAPIView.as_view()),

    #apps urls
    path('api/', include('api.urls')),
    path('api/users/', include('users.urls')),
    path('api/product/', include('products.urls')),
    path('api/search/', include('search.urls')),

    #documentation urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]