from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
