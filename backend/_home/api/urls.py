from django.urls import path
from .views import api_home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api'

urlpatterns =[
    path('', api_home),
    path('auth/', ObtainAuthToken.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]