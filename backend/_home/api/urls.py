from django.urls import path
from .views import api_home
from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api'

urlpatterns =[
    path('', api_home),
    path('auth/', ObtainAuthToken.as_view()),
]