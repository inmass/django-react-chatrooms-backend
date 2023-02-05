from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('jwt/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('rooms/', getRooms, name="rooms"),
    path('create-room/', createRoom, name="create-room"),
]
